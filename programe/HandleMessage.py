from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage
)
from linebot import (
    LineBotApi
)

def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=str(event)))