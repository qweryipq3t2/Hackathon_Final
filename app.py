import requests
from flask import Flask, request





PRODUCT_ID = "1189249f-cc67-4d47-b67e-a9c1bbcc5c3d"
API_KEY = "1189249f-cc67-4d47-b67e-a9c1bbcc5c3d"
MY_NGROK_URL = "https://jural-nondefectively-lidia.ngrok-free.dev/webhook"
sendt=[]

app = Flask(__name__)

def set_webhook():
    """Tells Maytapi to send WhatsApp messages to your ngrok URL."""
    url = f"https://api.maytapi.com/api/{PRODUCT_ID}/setWebhook"
    headers = {
        "Content-Type": "application/json",
        "x-maytapi-key": API_KEY
    }
    data = {"webhook": MY_NGROK_URL}
    
    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            print("✅ Success: Maytapi is now linked to your ngrok!")
        else:
            print(f"❌ Error setting webhook: {response.text}")
    except Exception as e:
        print(f"❌ Connection Error: {e}")

@app.route("/", methods=['GET', 'POST'])
def whatsapp_webhook():
    if request.method == 'GET':
        return " Fairness Engine is Live!", 200
    
    data = request.get_json()
    print("\n" + "="*40, flush=True)
    
    notifications = data if isinstance(data, list) else [data]

    for item in notifications:
        user = item.get('user', {})
        msg = item.get('message', {})
        category = item.get('type') 
        
        name = user.get('name', 'Unknown')
        print(f" RECEIVED: {category.upper()} FROM {name}", flush=True)

        if category == 'message':
            if 'text' in msg:
                print(f" TEXT: {msg.get('text')}", flush=True)
                sendt.append(msg.get('text'))
            
            if 'url' in msg:
                print(f" MEDIA URL: {msg.get('url')}", flush=True)
                
                
        elif category == 'text':
            print(f" TEXT: {msg.get('text')}", flush=True)
        elif category in ['ptt', 'audio']:
            print(f"VOICE NOTE: {msg.get('url')}", flush=True)

    print("="*40 + "\n", flush=True)
    return "OK", 200

if __name__ == "__main__":
    set_webhook()
    print("🚀 Server waiting for WhatsApp messages...")
    app.run(port=80)