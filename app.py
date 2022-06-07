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

line_bot_api = LineBotApi('phr2eC/k9BkpJ3xc+KbILDIkmYvS4ckxvNvHYch4Wp3wmLBPgvWsK7oVmZCT51drDr8MkhtJ9gpNq377zf41lv191OZwWUcWxjrCeZ8YfODtsUo7jgbI3VOvef7hGx/TTN1WLPSB3MKOzfnvcVLUfgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('173e1fa2e5f771bc54b049cba741e1aa')


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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    r = "很抱歉你在問什麼?"

    if msg == 'hi':
        r = 'hi'
    elif msg == '吃飽沒':
        r = '還沒'

    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text='你吃飽了嗎?'))


if __name__ == "__main__":
    app.run()