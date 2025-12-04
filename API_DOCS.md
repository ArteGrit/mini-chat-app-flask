# API Documentation for mini-chatgpt-app Backend

This document provides comprehensive API documentation for the mini-chatgpt-app backend. It details each endpoint's purpose, how to use it, expected inputs, and sample outputs.

## Health Module

<!-- Feature: Health Check -->
### GET /api/health

- **HTTP Method:** `GET`
- **Full Endpoint Path:** `/api/health`
- **Description:** Checks the operational status of the backend server. A successful response indicates that the server is running and accessible.
- **Request Parameters:** None
- **Request Example:**

  ```http
  GET /api/health
  ```

- **Response Structure (200 OK):**

  ```json
  {
    "status": "ok"
  }
  ```
- **Edge Cases/Errors:** No specific error cases are handled beyond standard network issues.
- **Authentication Requirements:** None

## User Management Module

<!-- Feature: List Users -->
### GET /api/users

- **HTTP Method:** `GET`
- **Full Endpoint Path:** `/api/users`
- **Description:** Retrieves a list of all currently registered users in the in-memory storage. Each user object includes their `user_id`, `first_name`, and `last_name`.
- **Request Parameters:** None
- **Request Example:**

  ```http
  GET /api/users
  ```

- **Response Structure (200 OK):**

  ```json
  {
    "generated-uuid-1": {
      "user_id": "generated-uuid-1",
      "first_name": "Bruce",
      "last_name": "Wayne"
    },
    "generated-uuid-2": {
      "user_id": "generated-uuid-2",
      "first_name": "John",
      "last_name": "Doe"
    }
  }
  ```
- **Edge Cases/Errors:** Returns an empty JSON object if no users are registered.
- **Authentication Requirements:** None

<!-- Feature: Create User -->
### POST /api/user

- **HTTP Method:** `POST`
- **Full Endpoint Path:** `/api/user`
- **Description:** Creates a new user entry in the in-memory storage and assigns a unique `user_id`. Optional `first_name` and `last_name` can be provided in the request body.
- **Request Parameters (Body):**
    - `first_name` (string, optional): The first name of the user. Defaults to "Bruce".
    - `last_name` (string, optional): The last name of the user. Defaults to "Wayne".
- **Request Example:**

  ```json
  {
    "first_name": "John",
    "last_name": "Doe"
  }
  ```

- **Response Structure (201 Created):**

  ```json
  {
    "user_id": "generated-uuid-string"
  }
  ```
- **Edge Cases/Errors:** Data is stored in-memory and will be lost upon server restart.
- **Authentication Requirements:** None

## Chat Module

<!-- Feature: Chat with AI -->
### POST /api/chat

- **HTTP Method:** `POST`
- **Full Endpoint Path:** `/api/chat`
- **Description:** Sends a user message to the integrated Google Gemini AI model and receives an AI-generated reply. It supports maintaining conversation history for a given `user_id` and allows selection between different Gemini models.
- **Request Parameters (Body):**
    - `message` (string, required): The user's message to the AI.
    - `user_id` (string, optional): A unique identifier for the user to maintain conversation history. If not provided, a temporary `user_id` will be assigned.
    - `model` (string, optional): The Gemini model to use. Accepted values are `"gemini-2.5"` (maps to `gemini-1.5-flash-latest`) or `"gemini-3"` (maps to `gemini-1.0-pro`). Defaults to `"gemini-2.5"`.
- **Request Example:**

  ```json
  {
    "user_id": "your-user-id",
    "message": "Tell me a story about a brave knight.",
    "model": "gemini-2.5"
  }
  ```

- **Response Structure (200 OK):**

  ```json
  {
    "reply": "The AI\'s response to your message.",
    "model_used": "gemini-2.5",
    "timestamp": "ISO-formatted-datetime-string"
  }
  ```
- **Edge Cases/Errors:**
    - `400 Bad Request`: If `message` is missing in the request body, or if an invalid `model` name is provided.
    - `500 Internal Server Error`: For unexpected issues during AI processing or server operations.
    - If `GEMINI_API_KEY` is not configured, mock responses will be returned.
- **Authentication Requirements:** None

<!-- Feature: View Chat History -->
### GET /api/chat/history

- **HTTP Method:** `GET`
- **Full Endpoint Path:** `/api/chat/history`
- **Description:** Retrieves the entire in-memory conversation history for all users. This is primarily for debugging and demonstration purposes.
- **Request Parameters:** None
- **Request Example:**

  ```http
  GET /api/chat/history
  ```

- **Response Structure (200 OK):**

  ```json
  {
    "user-id-1": [
      {"role": "user", "text": "Hello"},
      {"role": "assistant", "text": "Hi there!"}
    ],
    "temp_user_1678881234": [
      {"role": "user", "text": "What is your name?"},
      {"role": "assistant", "text": "I am a large language model, trained by Google."}
    ]
  }
  ```
- **Edge Cases/Errors:** Returns an empty JSON object if no conversations have occurred.
- **Authentication Requirements:** None
