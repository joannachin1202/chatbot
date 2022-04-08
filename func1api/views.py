from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage , TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction
from module import func


from linebot.models import PostbackEvent
from urllib.parse import parse_qsl

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

x=0
tem=[]
student_id=list(func.arrange_data('number1.csv'))

@csrf_exempt
def callback(request):
    global x
    global tem
    global text
    global rows
    global text_intersection
    global stu_id_intersection
    
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
                    
                    
                    if mtext == '兔子': #希望調整成只要輸入任意文字都會回覆
                        func.begin(event)  
                        
                    elif mtext == '承辦人員資訊':
                         func.聯絡人資訊(event)
                    
                    elif mtext == '應修課程':
                         func.應修課程(event)
                         
                    elif mtext == '申請條件':
                         func.申請條件(event)
                    
                    elif mtext == '本學期開課':
                         func.本學期開課(event)
                    
                    elif mtext == '好呀！':
                         func.提供關鍵詞(event)
                         x+=1
                    
                    elif mtext == '先不用':
                       line_bot_api.reply_message(event.reply_token,TextSendMessage(text='希望這些推薦能幫你找到合胃口的跨領域紅蘿蔔！\n謝謝你願意和我聊天當朋友，若你想了解更多跨域森林或各個蘿蔔坑的資訊，可以在下方的選單找森林裡的其他朋友了解相關功能喔！\n隨時歡迎你呼喊我的名字「小圖」，回來找我聊天喔～'))
                        
                    #要看 tem 有多長用 len（）
                    # 當長度是三時我
                    elif x==1:
                        tem.append(mtext)
                        if len(tem)==3:
                            text_intersection = tem
                            content=func.subject(tem)
                            x-=1
                            tem=[]
                            #清除
                            message = [  #串列
                                TextSendMessage(  
                                text = 'yum yum～待我細細回想這滋味...'
                                ), 
                                TextSendMessage(  
                                text = content
                                ), 
                                TextSendMessage(  
                                text = "快看！前面就是校務中心大榕樹了，聽說只要取得樹洞裡的UCAN測驗果實，再搭配先前從籃子中選取的跨域紅蘿蔔，就有機會找到整座森林中同時符合自身口味和興趣測驗結果的紅蘿蔔，讓我們一起來試試吧！"
                                ),
                                TextSendMessage(  
                                text = "接下來將依據你最近一次透過UCAN平台進行職涯興趣測驗時，存放在校務資料中心樹洞裡的測驗果實來幫助你探索森林，請輸入你的學號讓我為你找出你的測驗果實吧～"
                                )
                     
                              ]
          
                            line_bot_api.reply_message(event.reply_token,message)
            
                    elif mtext == '先等等':
                        func.先不用(event)
                    elif mtext == '出發囉':
                        
                        func.提供關鍵詞(event)
                        x+=1
                    
                    elif mtext == '回跨域紅蘿蔔':
                        
                        func.提供關鍵詞(event)
                        x+=1
                    
                    elif mtext == '交集':
                        subject_ans = func.subject(text_intersection)
                        rows = func.arrange_data('number1.csv') 
                        
                        holand_ans = func.return_course(func.get_quiz_results(stu_id_intersection,rows))
                        output=func.get_connection(subject_ans,holand_ans)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=output))     
    
                
                    elif mtext in student_id:
                        rows = func.arrange_data('number1.csv')
                        stu_id_intersection = mtext
                        holand=func.return_course(func.get_quiz_results(mtext,rows))
                        
                        subject_ans = func.subject(text_intersection)
                        holand_ans = func.return_course(func.get_quiz_results(stu_id_intersection,rows))
                        output=func.get_connection(subject_ans,holand_ans)
                        
                        message = [  #串列
                                TextSendMessage(  
                                text = '感謝你！\n我在樹洞裡找到了與你學號相對應的測驗果實~'
                                ), 
                                TextSendMessage( 
                                text = output
                                ),
                                TemplateSendMessage(
                                alt_text='重玩一次？',
                                template=ConfirmTemplate(
                                text='跨域森林很大，總共蘊含了六十個不同品種的紅蘿蔔，要不要讓我們再探索不同品種的紅蘿蔔呢？',  #主標題
                                actions=[    
                                MessageTemplateAction(  
                                label='先不用', #按鈕文字
                                text='先不用' #顯示文字計息  
                                ),
                                MessageTemplateAction(  #顯示文字計息
                                label='好呀！',
                                text='好呀！'
                                )
                     
                               ]
                             )
                           )
        
                         ]
          
                        line_bot_api.reply_message(event.reply_token,message)
          
                        line_bot_api.reply_message(event.reply_token,message)
                   
                  
            
                  

















                   

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
