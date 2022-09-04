# from argparse import ArgumentParser
# from re import A

from flask import Flask, request, abort
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, 
    PostbackEvent, FlexSendMessage,
)

from Constants.ChannelCode import getChannelToken, getChannelSecret
from Constants.FlexMessage import getFlexMessage
from Constants.spreadsheet import getData

app = Flask(__name__)

line_bot_api = LineBotApi(getChannelToken())
handler = WebhookHandler(getChannelSecret())
FLASHCARD_ORDER, SPELLING_ORDER = 0,0
FLEX = getFlexMessage()
DATA_FLASHCARD, DATA_SPELLING = getData()
ADDWORD = False
SPELLING = False

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
        TextSendMessage(event.message.text))
    # global SPELLING_ORDER, SPELLING
    # if (event.message.text == (DATA_SPELLING['korean'][SPELLING_ORDER]) and SPELLING):
    #     update_data(DATA_SPELLING['thai'][SPELLING_ORDER], True, "spelling")
    #     if SPELLING_ORDER + 1 < len(DATA_SPELLING['korean']):
    #         SPELLING_ORDER += 1
    #     else:
    #         SPELLING_ORDER = 0
    #     line_bot_api.reply_message(
    #             event.reply_token,
    #             TextSendMessage("SPELLING: "+DATA_SPELLING['thai'][SPELLING_ORDER]))
    # elif (event.message.text != (DATA_SPELLING['korean'][SPELLING_ORDER]) and SPELLING):
    #     update_data(DATA_SPELLING['thai'][SPELLING_ORDER], False, "spelling")
    #     if SPELLING_ORDER + 1 < len(DATA_SPELLING['korean']):
    #         SPELLING_ORDER += 1
    #     else:
    #         SPELLING_ORDER = 0
    #     line_bot_api.reply_message(
    #             event.reply_token,
    #             [TextSendMessage("CORRECT ANS: " + DATA_SPELLING['thai'][SPELLING_ORDER-1]),
    #             TextSendMessage("SPELLING: "+DATA_SPELLING['thai'][SPELLING_ORDER])])
    # elif ADDWORD:
    #     if SPELLING:
    #         SPELLING = False
    #     new_word = event.message.text.split(":")
    #     add_word(new_word[0].rstrip().lstrip(), new_word[1].rstrip().lstrip())
    

# @handler.add(PostbackEvent)
# def handle_event(event):
#     global FLASHCARD_ORDER,SPELLING, SPELLING_ORDER, ADDWORD
#     if (event.postback.data == ('flash_card')):
#         if SPELLING or ADDWORD:
#             SPELLING = False
#             ADDWORD = False
#         FLASHCARD_ORDER = 0
#         FLEX['body']['contents'][0]['text'] = DATA_FLASHCARD['korean'][FLASHCARD_ORDER]
#         line_bot_api.reply_message(
#             event.reply_token,
#             FlexSendMessage(alt_text="flash card",contents=FLEX))
#     elif (event.postback.data == ('know')):
#         update_data(DATA_FLASHCARD['korean'][FLASHCARD_ORDER], True, "flashcard")
#         if FLASHCARD_ORDER + 1 < len(DATA_FLASHCARD['korean']):
#             FLASHCARD_ORDER += 1
#         else:
#             FLASHCARD_ORDER = 0
#         FLEX['body']['contents'][0]['text'] = DATA_FLASHCARD['korean'][FLASHCARD_ORDER]
#         line_bot_api.reply_message(
#             event.reply_token,
#             [TextSendMessage(text=DATA_FLASHCARD['thai'][FLASHCARD_ORDER-1]),
#             FlexSendMessage(alt_text="flash card",contents=FLEX)])
#     elif (event.postback.data == ('dont know')):
#         update_data(DATA_FLASHCARD['korean'][FLASHCARD_ORDER], False,"flashcard")
#         if FLASHCARD_ORDER + 1 < len(DATA_FLASHCARD['korean']):
#             FLASHCARD_ORDER += 1
#         else:
#             FLASHCARD_ORDER = 0
#         FLEX['body']['contents'][0]['text'] = DATA_FLASHCARD['korean'][FLASHCARD_ORDER]
#         line_bot_api.reply_message(
#             event.reply_token,
#             [TextSendMessage(text=DATA_FLASHCARD['thai'][FLASHCARD_ORDER-1]),
#             FlexSendMessage(alt_text="flash card",contents=FLEX)])
#     elif (event.postback.data == ('spelling')):
#         SPELLING_ORDER = 0
#         SPELLING = not SPELLING
#         if ADDWORD:
#             ADDWORD = False
#         if SPELLING:
#             line_bot_api.reply_message(
#                 event.reply_token,
#                 TextSendMessage(text="SPELLING: " + DATA_SPELLING['thai'][SPELLING_ORDER]))
#         else:
#             line_bot_api.reply_message(
#                 event.reply_token,
#                 TextSendMessage(text="SPELLING: False"))

#     elif (event.postback.data == ('add_word')):
#         ADDWORD = not ADDWORD
#         line_bot_api.reply_message(
#             event.reply_token,
#             TextSendMessage(text=f"ADD WORD: {ADDWORD}"))

        
if __name__ == "__main__":
    # arg_parser = ArgumentParser(
    #     usage='Usage: python ' + __file__ + ' [--port <port>] [--help]'
    # )
    # arg_parser.add_argument('-p', '--port', default=8000, help='port')
    # arg_parser.add_argument('-d', '--debug', default=False, help='debug')
    # options = arg_parser.parse_args()

    # app.run(debug=options.debug, port=options.port)
    app.run(debug=False)


