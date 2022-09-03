from crypt import methods
from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, FlexSendMessage,
    URIAction, ImageComponent, BubbleContainer
)
import json

from Constants.ChannelCode import *
from Constants.FlexMessage import *

app = Flask(__name__)

line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)

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
        FlexSendMessage(
    alt_text='hello',
    contents=BubbleContainer(
        direction='ltr',
        hero=ImageComponent(
            url='https://example.com/cafe.jpg',
            size='full',
            aspect_ratio='20:13',
            aspect_mode='cover',
            action=URIAction(uri='http://example.com', label='label')
                            )
                        )
                    )     
        )
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
    flex = json.loads(flexmessage())

        
if __name__ == "__main__":
    app.run(debug=False)



