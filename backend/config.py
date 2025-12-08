import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'a_very_secret_key'
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')

    # Recommended defaults for new SDK
    GEMINI_2_5_MODEL = os.environ.get('GEMINI_FAST_MODEL') or 'gemini-2.5-flash'
    GEMINI_3_MODEL = os.environ.get('GEMINI_PRO_MODEL') or 'gemini-3-pro-preview'

