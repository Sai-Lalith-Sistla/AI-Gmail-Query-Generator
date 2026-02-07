# Accelerating Development with Agentic Pair Programming: My DevDay Buildathon Experience 🚀

I had planned a complex 20-pager app to demonstrate agentic workflows, but I quickly realized that solo-developing it from scratch would be a massive time sink. I needed a way to move faster.

That's when I saw an email land in my inbox on "Buildathon using Intelligent Engineering Principles – For the Love of Building" by Sahaj Software.

**About the Event: DevDay – For the Love of Building**
This wasn't a traditional hackathon. No fixed problem statements. No pressure to compete. Just a day off from deadlines to build what "we always wanted to build."
The only expectation? Build using **Intelligent Engineering practices** that leverage AI-assisted coding tools. It’s about exploring how modern engineers can think better, move faster, and build smarter with AI as a collaborator.

Big congratulations to the Sahaj team for their new office space in Hyderabad located in the Sky City building, Gachibowli! 🏢✨

For this buildathon, I knew I couldn't build my massive 20-pager app in a single day. But with determination to solve one of my daily problems, I swiftly thought of the troubles I face with 1000+ emails every week. The time it takes to delete them, sort them across folders... sure, I use search/filter patterns, but sometimes even important emails or coupons of interest get lost in the noise.

So I took that as my topic to build!

My choice of tool? Among GitHub Copilot, Cursor, Claude Desktop, or Codeium, I chose **Antigravity** (Google's agentic AI) cause it's free 😛.

The day started with Karun Japhet sharing how he solved a problem using Intelligent Engineering principles. The hour-long talk included how he structured project information and the use of LLMs with context in mind—it really shed new light for me.

With that as an anchor, I built my project. There were ups and downs, surprises at every turn, and a lot of learning to take home.

**Technical Learnings & Take homes**

One of the key decisions I made was to use the **Model Context Protocol (MCP)** to fetch emails, rather than standard Google APIs.
Why? -- I wanted to push my learning. MCP provides a standardized interface for model tools, outsourcing the complex auth/token lifecycle to a specialized server.
But the Challenge: Getting Python (backend) to talk to a Node.js-based MCP server on Windows was tricky! I dealt with `WinError 2` (missing `npx` paths) and environment variable "blindness" in subprocesses. I installed Node.js and npx, and then I was able to use the MCP server to fetch emails. No thanks to Antigravity's documentation which was not helpful at all.

**Privacy & Security First:** I picked up some critical safety practices during the event, specifically regarding how we cannot easily stop an agent from reading any and all files in its workspace—meaning `.env` files are never truly an exception. Learning from others' mistakes and determined not to let my credentials be leaked, I brainstormed with the folks there. While we formulated some excellent ideas for enterprise production environments, I decided to pivot to a UI-based auth system for this build. By eliminating `.env` files and storing keys only in session state, I ensured better security—cause who knows where those `.env` files end up! 😅

**The Importance of Clear Guidelines**
Success in agentic workflows relies heavily on how we structure project context and define explicit "rules" for the build. I’ve come to view AI as an **"eager intern"**: full of energy but lacking direction. Without a clear set of established coding practices, the probabilistic nature of LLM outputs can easily result in code that falls short of production standards. The best outcomes emerge when you break down complex architectures into smaller, manageable problems and maintain a tight loop of observation, implementation, and testing. This structured approach ensures that even complex integrations, like MCP servers, are handled with technical rigor and security in mind.

It was a day dedicated to building something I care about, with people who care just as much.


#DevDay #SahajSoftware #IntelligentEngineering #AI #Buildathon #Antigravity #GoogleMCP #Streamlit #Python #Coding #Hyderabad
