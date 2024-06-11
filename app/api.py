# app/api.py
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # 加载环境变量

API_URL = "https://api.coze.cn/open_api/v2/chat"
API_TOKEN = os.getenv("API_TOKEN")
BOT_ID = os.getenv("BOT_ID")

def get_response_from_api(message):
    headers = {
        "Authorization": f"Bearer {API_TOKEN}",
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Host": "api.coze.cn",
        "Connection": "keep-alive"
    }
    payload = {
        "bot_id": BOT_ID,
        "user": "123333333",
        "query": message,
        "stream": False
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # 打印响应以检查格式
    print(response.json())
    
    return response.json()
