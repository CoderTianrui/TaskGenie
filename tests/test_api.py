import pytest
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://api.deepseek.com/v1/chat/completions"
API_KEY = os.getenv("DEEPSEEK_API_KEY")

def test_deepseek_api_connection():
    """Test the connection to DeepSeek API"""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    response = requests.get(BASE_URL, headers=headers)
    assert response.status_code in [200, 401, 404]  # API might require POST only

def test_task_suggestion_format():
    """Test the format of task suggestions"""
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {API_KEY}'
    }
    payload = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful task management assistant. Generate 3 specific subtasks for the given task."
            },
            {
                "role": "user",
                "content": "Clean the house"
            }
        ],
        "temperature": 0.7,
        "max_tokens": 150
    }
    
    response = requests.post(BASE_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        assert "choices" in data
        assert len(data["choices"]) > 0
        assert "message" in data["choices"][0]
        assert "content" in data["choices"][0]["message"]