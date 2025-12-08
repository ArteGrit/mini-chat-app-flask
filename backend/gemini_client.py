from google import genai
import random

class GeminiClient:
    def __init__(self, config):
        self.config = config
        self.api_key = self.config.GEMINI_API_KEY

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
            self.client = genai.Client(api_key=self.api_key)
        else:
            self.client = None

    def get_model(self, model_name):
        if not self.api_key:
            return None

        if model_name == "gemini-2.5":
            return self.config.GEMINI_2_5_MODEL
        elif model_name == "gemini-3":
            return self.config.GEMINI_3_MODEL
        else:
            raise ValueError("Invalid model name specified.")

    def send_message(self, history, message, model_name = "gemini-2.5-flash"):
        try:

            if not self.api_key:
                return random.choice(self.mock_answers)

            model = self.get_model(model_name)
            print('API_KEY', self.api_key, model)

            chat = self.client.chats.create(model=model)

            # If you have previous history (list of messages), replay it
            for item in history:
                chat.send_message(item["text"])

                # Send the new message
            response = chat.send_message(message)

            # response = chat.send_message(message)

            for message in chat.get_history():
                print(f'role - {message.role}', end=": ")
                print(message.parts[0].text)

            return response.text

        except Exception as e:
            print("Exception caught in send_message:", e)
            return f"Error: {e}"
