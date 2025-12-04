import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    GEMINI_2_5_MODEL = os.environ.get('GEMINI_2_5_MODEL') or 'gemini-1.5-flash-latest'
    GEMINI_3_MODEL = os.environ.get('GEMINI_3_MODEL') or 'gemini-1.0-pro'
