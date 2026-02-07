# 🚀 **Came here from my post?**

You might want to read these in order:

1. 📘 [My DevDay Buildathon Experience](./linkedin_post_1.md)
2. ⚙️ [My Approach](./linkedin_post_2.md)






# Gmail AI Segregator (Inbox AI)

A premium email intelligence tool helping you analyze, tag, and query your inbox using AI.
Built with **Streamlit**, **Flask**, **Google Gemini**, and **Google MCP**.

## Features

-   **🛡️ Smart Sensitivity Masking**: Two-stage analysis scans headers first. Sensitive emails (like banking/healthcare) are hidden from the UI body view for privacy.
-   **🏷️ Custom Tag Management**: Create and manage custom tags (e.g., "LLM", "System Design") stored locally.
-   **🔍 AI Query Generator**: Generate complex Gmail search queries (e.g., `(subject:"system design" OR from:engineering-blog.com) label:unread`) using selected tags.
-   **📂 Local Data Persistence**: Fast viewing with local caching of fetched emails.
-   **📺 Dashboard**: One-click analysis and category expansion.

## Prerequisites

-   **Python 3.8+**
-   **Node.js & NPM**: Required for the underlying Google MCP server execution. Ensure `npx` is available in your terminal.

## Installation

1.  **Clone the repository**:
    ```bash
    git clone <repository-url>
    cd <repository-name>
    ```

2.  **Install Python Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3.  **Ensure Node.js is installed**:
    Run `node -v` and `npm -v` to verify.

## 🚀 Getting Started

### 1. Secure Authentication Setup

> [!NOTE]
> **Privacy First**: Your keys are entered directly in the web UI and stored only in your browser's session memory. No `.env` file is strictly required for keys.

To get your credentials:

#### **A. Google Gemini API Key**
1.  Go to [Google AI Studio](https://aistudio.google.com/).
2.  Click **Get API key**.
3.  Create a new key and copy it.

#### **B. Google OAuth Credentials (Gmail)**
1.  Go to the [Google Cloud Console](https://console.cloud.google.com/).
2.  Create a new project.
3.  Enable the **Gmail API** in "APIs & Services" > "Library".
4.  Go to "APIs & Services" > "OAuth consent screen".
    *   Choose "External" and fill in the required app info.
    *   Add the scope: `https://www.googleapis.com/auth/gmail.readonly`.
5.  Go to "APIs & Services" > "Credentials".
    *   Click **Create Credentials** > **OAuth client ID**.
    *   Application type: **Desktop app**.
6.  Copy the **Client ID** and **Client Secret**.

### 2. Launching the App

Open two terminal instances:

**Terminal 1 (Backend):**
```bash
cd backend
python app.py
```

**Terminal 2 (Frontend):**
```bash
cd frontend
streamlit run app.py
```

### 3. Usage
1.  You will arrive at the **🏠 Home** page.
2.  Click **Get Started** or navigate to **🔐 Setup** in the sidebar.
3.  Enter your **Gemini API Key**, **Client ID**, and **Client Secret**.
4.  Start analyzing your inbox!

## 🛠️ Troubleshooting

-   **WinError 2**: If you see this, ensure **Node.js** is installed and `npx` is in your PATH. The app tries to find it automatically, but it is a prerequisite.
-   **MCP Timeout**: The first run might take ~30 seconds to download the Gmail MCP server. Please be patient.
