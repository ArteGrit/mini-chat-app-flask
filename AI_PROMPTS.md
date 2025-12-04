# AI Prompts for mini-chatgpt-app Backend

The prompts reference the required features:
- Flask backend
- `/api/chat`, `/api/user`, `/api/health` endpoints
- Gemini 2.5 / Gemini 3 model selection
- In-memory user + conversation storage
- Separate Gemini client module
- Environment variables for configuration
- Clear and simple explanations in the code

---

### **Prompt — Create the complete project structure**

I understand backend architecture, but I am not familiar with how a Python/Flask project should be organized.  
Based on the technical assignment, please generate a full project structure for a Flask backend that supports these endpoints: `/api/chat`, `/api/user`, `/api/health`.

The project must include:
- a main Flask entry point
- separate route modules (`routes/`)
- in-memory storage module (`storage/`)
- a Gemini client module (`gemini_client.py`)
- configuration handling with environment variables
- files for documentation (`API_DOCS.md`, `AI_PROMPTS.md`)
- `.env.example`  
- explanations of what each file and folder is for

Generate all folders and empty files, along with a short explanation of the architecture.

---

### **Prompt — Implement in-memory storage and user creation**

The backend must store users and their conversation history in memory.

Please generate:
- a `storage/memory.py` module with:
  - a dictionary of users
  - a dictionary of conversation_history

- the `/api/user` route that uses users storage, saves simple user { user_id:... } and returns `{ "user_id": ... }`

---

### **Prompt — Create the Gemini client module**

Please generate a standalone `gemini_client.py` module that:

- accepts a model name (`"gemini-2.5"` or `"gemini-3"`)
- maps it to internal model IDs
- supports real communication with Google Gemini (if API key is available)
- supports mock mode (if no API key is provided)

Mock mode should return a simple deterministic mocked answer, so the backend works without a real API key.

Add comments explaining how the module works and how the `/api/chat` endpoint uses it.

---

### **Prompt — Create the /api/chat endpoint**

Please generate the `/api/chat` route using Flask.

The endpoint must:
- accept JSON with: `user_id`, `message`, `model`
- validate the request (return 400 if message is missing)
- load user history from memory
- save the new user message
- call the Gemini client to generate a reply
- save the assistant reply
- return JSON with:
  - `reply`
  - `model_used`
  - `timestamp`

---

### **Prompt — generate `API_DOCS.md`**
analyze all files in the current repository and generate a Markdown file named `API_DOCS.md`.
Requirements:
1. For every API route, endpoint, or HTTP handler in the repository, generate a documentation block.

2. Each block should include:
   - The **feature or module name** as a comment above the block. Example:
   - HTTP method (GET, POST, etc.)
   - Full endpoint path (e.g., /api/user)
   - Request parameters (body, query, headers)
   - Request example (JSON if applicable)
   - Response structure (JSON example, status codes)
   - Description of the endpoint’s purpose and behavior
   - Any edge cases, errors, or authentication requirements

3. Organize the Markdown file hierarchically if useful (group endpoints by module or feature).

4. Include **all relevant API endpoints**; do not invent endpoints that are not in the code.

5. Format example:



