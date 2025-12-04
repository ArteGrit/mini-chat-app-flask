import google.generativeai as genai
import random

class GeminiClient:
    def __init__(self, config):
        self.config = config
        self.api_key = self.config.GEMINI_API_KEY

        # Mock responses used when no API key is provided
        self.mock_answers = [
            "This is a mock response generated because no API key was provided. "
            "In a real scenario, this message would come from a Gemini model.",

            "Since the AI model is unavailable, here is a simulated answer. "
            "You can customize this placeholder text as needed.",

            "I'm responding with a mock message because the system is running "
            "in offline mode. Add an API key to enable real AI-generated replies.",

            "This is a fallback mock reply. The Gemini model was not initialized, "
            "so you're seeing this simulated output instead.",

            "Mock data activated — the request could not be processed by the actual model. "
            "Feel free to adjust the mock responses for testing or development.",
        ]

        # Only configure SDK if API key exists
        if self.api_key:
            genai.configure(api_key=self.api_key)

    def get_model(self, model_name):
        # If no API key, return None since model cannot be initialized
        if not self.api_key:
            return None

        if model_name == "gemini-2.5":
            return genai.GenerativeModel(self.config.GEMINI_2_5_MODEL)
        elif model_name == "gemini-3":
            return genai.GenerativeModel(self.config.GEMINI_3_MODEL)
        else:
            raise ValueError("Invalid model name specified.")

    def send_message(self, history, message, model_name):
        # Mock mode — return a random mock message
        if not self.api_key:
            return random.choice(self.mock_answers)

        # Normal Gemini mode
        model = self.get_model(model_name)

        # Convert memory history to Gemini chat format
        chat_history_for_gemini = [
            {"role": item["role"], "parts": [item["text"]]}
            for item in history
        ]

        chat = model.start_chat(history=chat_history_for_gemini)

        response = chat.send_message(message)
        return response.text
