from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage , TextSendMessage
from module import func


from linebot.models import PostbackEvent
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

x=0
tem=[]
student_id=list(func.arrange_data(r'/Users/ChinJungAn/linechatbot/linebotFunc1拷貝/func1api/number1.csv'))

@csrf_exempt
def callback(request):
    global x
    global tem
    
    if request.method == 'POST':
        message=[]
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text
                    if mtext == '嗨': #希望調整成只要輸入任意文字都會回覆
                        func.begin(event)         
                        
                    #要看 tem 有多長用 len（）
                    # 當長度是三時我
                    elif x==1:
                        tem.append(mtext)
                        if len(tem)==3:
                            
                            content=func.subject(tem)
                            x-=1
                            tem=[]
                            #清除
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=content))     
                    
                    elif mtext == '想試試':
                        func.想試試(event)
                    elif mtext == '先不用':
                        func.先不用(event)
                    elif mtext == '跨領域學習':
                        func.提供關鍵詞(event)
                        x+=1
    
                        
                    elif mtext =='與自身所學相關':
                        func.提供關鍵詞(event)
                    
                    
                    elif mtext in student_id:
                        rows = func.arrange_data(r'/Users/ChinJungAn/linechatbot/linebotFunc1拷貝/func1api/number1.csv')
                        
                        holand=func.return_course(func.get_quiz_results(mtext,rows))
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=holand))     
                        
                        
                  
            
                  

















                   

            if isinstance(event, PostbackEvent):  #PostbackTemplateAction觸發此事件
                backdata = dict(parse_qsl(event.postback.data))  #取得Postback資料
                if backdata.get('action') == '+':
                    func.sendBack_加(event, backdata)
                elif backdata.get('action') == 'sell':
                    func.sendBack_sell(event, backdata)

                elif backdata.get('action') == 'sells':
                    func.sendData_sell(event, backdata)

        return HttpResponse()

    else:
        return HttpResponseBadRequest()
