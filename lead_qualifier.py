import os
import requests
from dotenv import load_dotenv
import json

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-3.5-flash-lite:generateContent"

headers ={
    "x-goog-api-key":API_KEY,
    "content-type": "apllication/json"

}

lead_message = input("Enter the lead's message: ")

prompt = f"""
You are a qualification assistant. Respond only with JSON, using exactly this two keys:
"label": Hot, Warm, or cold
"reply": a short, friendly reply to the lead

Message:{lead_message}
"""

data = {
    "contents": [
        {"parts": [{"text": prompt}]}
    ],
    "generationConfig": {"responseMimeType": "application/json"}
}

response = requests.post(url, headers=headers, json=data, timeout=30)

result = response.json()

if "error" in result:
    print("Something went wrong:", result["error"]["message"])
else:
    reply_text = result["candidates"][0]["content"]["parts"][0]["text"]
    answer = json.loads(reply_text)
    print("Label:", answer["label"])
    print("Reply:", answer["reply"])

with open("leads_log.txt", "a") as file:
    file.write(f"Lead: {lead_message}\n")
    file.write(f"Label: {answer['label']}\n")
    file.write(f"Reply: {answer['reply']}\n")
    file.write("---\n")