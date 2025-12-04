from flask import Blueprint, request, jsonify
from datetime import datetime
from ..gemini_client import GeminiClient
from ..config import Config
from ..storage.memory import conversation_history

bp = Blueprint('chat', __name__, url_prefix='/api')

gemini_client = GeminiClient(Config)

@bp.route('/chat/history', methods=['GET'])
def list_users():
    return jsonify(conversation_history)

@bp.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_id = data.get('user_id')
    message = data.get('message')
    model_name = data.get('model', 'gemini-2.5')

    if not message:
        return jsonify({"error": "Message is required."}), 400

    # Assign a temporary user_id if not provided
    if not user_id:
        user_id = "temp_user_" + str(datetime.now().timestamp())

    # Initialize history for this user if not exists
    if user_id not in conversation_history:
        conversation_history[user_id] = []

    # Save user message into memory
    conversation_history[user_id].append({
        "role": "user",
        "text": message
    })

    try:
        # Pass the existing history into Gemini client (read-only)
        ai_reply = gemini_client.send_message(
            history=conversation_history[user_id],
            message=message,
            model_name=model_name
        )

        # Save AI reply to memory
        conversation_history[user_id].append({
            "role": "assistant",
            "text": ai_reply
        })

        return jsonify({
            "reply": ai_reply,
            "model_used": model_name,
            "timestamp": datetime.now().isoformat()
        })
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "An unexpected error occurred."}), 500
