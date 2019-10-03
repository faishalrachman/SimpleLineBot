import os
from flask import Flask, request, abort
import json

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
    SourceUser, SourceGroup, SourceRoom,
    TemplateSendMessage, ConfirmTemplate, MessageTemplateAction,
    ButtonsTemplate, ImageCarouselTemplate, ImageCarouselColumn, URITemplateAction,
    PostbackTemplateAction, DatetimePickerTemplateAction,
    CarouselTemplate, CarouselColumn, PostbackEvent,
    StickerMessage, StickerSendMessage, LocationMessage, LocationSendMessage,
    ImageMessage, VideoMessage, AudioMessage, FileMessage,
    UnfollowEvent, FollowEvent, JoinEvent, LeaveEvent, BeaconEvent
)


app = Flask(__name__)

line_bot_api = LineBotApi(
    'SPld+JxNSxnV1esL0amZGU1xBsKLEMKNmhx5XfcO67MCnFElmXjAIF/TYCZZNASTucRv85xnz07ePmxc38/zwWfcLriA1RggLjIkIWv7tBZ7UTQ4NUODQnZ+p72GNU+0I9h399KUPJdopiqDv57S/gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('bef1851dadab92779f602ddf91f2fe2f')

idipat = "U0f6f4d0357eb752c991b22cc2400e141"

@app.route("/callback", methods=['POST'])
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
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    text = event.message.text

@handler.add(JoinEvent)
def handle_join(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='Hai Aku Bukan Kerang ajaib :P'))

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    print ("server start")
    app.run(host='0.0.0.0', port=port)