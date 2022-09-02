from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('A/LutxhuQ5rBx5XTmfo5CyEZA4ov5ijZ7L7KuVzhLEHEVYIvnJV8+XAbvnUtjWfvu60ilWdfR6abusJkuLBNA4TDOGBN1OnSK+qkMTZf8ZzGi3m0oBy5kOzOS6CTc8fZ5mTUULWfWuP39dYo6NynqQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('65cdcfc23c498613eda60112b5de9421')

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

@app.route('/')
def hello():
    return "Hello Flask-Heroku"

@app.route('/callback', methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(event)))
        
if __name__ == "__main__":
    app.run(debug=False)