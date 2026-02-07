import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client
import os
from dotenv import load_dotenv
import traceback

load_dotenv()

class GmailMCPService:
    def _get_params(self, client_id, client_secret):
        import shutil
        try:
            npx_path = shutil.which("npx")
            if not npx_path:
                print("❌ ERROR: 'npx' not found. Please install Node.js (https://nodejs.org/) to use Gmail AI tools.")
                # We still return 'npx' to allow the subprocess to attempt and fail naturally with a clear OS error
                npx_path = "npx" 
            return StdioServerParameters(
                command=npx_path,
                args=["-y", "@modelcontextprotocol/server-gmail"],
                env={
                    "GOOGLE_CLIENT_ID": client_id,
                    "GOOGLE_CLIENT_SECRET": client_secret,
                    "PATH": os.getenv("PATH")
                }
        )
        except Exception as e:
            print(f"⚠️ WARNING: Error checking for 'npx': {e}")
            npx_path = "npx"
            
        

    async def fetch_labels(self, client_id, client_secret):
        try:
            params = self._get_params(client_id, client_secret)
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    result = await session.call_tool("list_labels", {})
                    return result.content if hasattr(result, 'content') else result
        except Exception as e:
            print(f"❌ Error in fetch_labels: {e}")
            traceback.print_exc()
            return {"error": str(e)}

    async def fetch_recent_emails(self, client_id, client_secret, count=20, label=None, unread_only=True):
        try:
            params = self._get_params(client_id, client_secret)
            async with stdio_client(params) as (read, write):
                async with ClientSession(read, write) as session:
                    await session.initialize()
                    
                    query = "is:unread" if unread_only else ""
                    if label:
                        query += f" label:{label.replace(' ', '-')}" # Simple slugging if needed
                    
                    result = await session.call_tool("search_emails", {
                        "q": query.strip(),
                        "max_results": count
                    })
                    
                    return result.content if hasattr(result, 'content') else result
        except Exception as e:
            print(f"❌ Error in fetch_recent_emails: {e}")
            traceback.print_exc()
            return {"error": str(e)}

    def get_labels_sync(self, client_id, client_secret):
        try:
            return asyncio.run(self.fetch_labels(client_id, client_secret))
        except Exception as e:
            return {"error": f"Failed to list labels: {e}"}

    def get_emails_sync(self, client_id, client_secret, count=20, label=None, unread_only=True):
        try:
            return asyncio.run(self.fetch_recent_emails(client_id, client_secret, count, label, unread_only))
        except Exception as e:
            return {"error": f"Failed to connect to Gmail MCP: {e}"}

gmail_service = GmailMCPService()
