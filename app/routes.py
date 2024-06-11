# app/routes.py
from flask import Blueprint, render_template, request, jsonify
from .api import get_response_from_api
from flask_misaka import Misaka

misaka = Misaka(safe_mode='yes')

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    api_response = get_response_from_api(user_input)
    
    # 解析响应中的 messages 数组并提取 content
    messages = api_response.get("messages", [])
    if messages:
        response_text = messages[0].get("content", "未定义的响应")
    else:
        response_text = "未定义的响应"
    
    rendered_text = misaka.render(response_text)
    
    return jsonify({"response": rendered_text})
