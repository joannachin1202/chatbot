from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage , TextSendMessage
from linebot.models import TextSendMessage
from linebot.models import TemplateSendMessage, MessageTemplateAction, ButtonsTemplate,ConfirmTemplate, PostbackTemplateAction,PostbackAction
from linebot.models import ImagemapSendMessage, BaseSize, ImagemapAction, ImagemapArea, MessageImagemapAction
from module import func


from linebot.models import PostbackEvent
from urllib.parse import parse_qsl
import time

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
    global holand_ans
    global output
    
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
                    if mtext == '兔子' or '兔' or '小兔' or '小兔子' or 'rabbit': #希望調整成只要輸入任意文字都會回覆
                        func.begin(event)
                    
                    #要看 tem 有多長用 len（）
                    # 當長度是三時我
                    if x==1:
                        tem.append(mtext)
                    elif len(tem)==3:
                            text_intersection = tem
                            content=func.subject(tem)
                            x-=1
                            tem=[]
                            #清除
                            message = [  #串列
                                TextSendMessage(  
                                text = 'yum yum～待我細細回想這滋味...'
                                ), 
                                time.sleep(3),
                                TextSendMessage(  
                                text = content
                                ), 
                                time.sleep(5),
                                TemplateSendMessage(
                                alt_text='選擇紅蘿蔔坑',
                                template=ButtonsTemplate(
                                text='在以上的推薦中，你覺得哪一區域的蘿蔔坑最符合你的發展目標或興趣呢？',  #主標題
                                actions=[    
                                MessageTemplateAction(  
                                label='雙修輔系灌木叢', #按鈕文字
                                text='雙修輔系灌木叢' #顯示文字計息  
                                 ),
                                MessageTemplateAction(  #顯示文字計息
                                label='跨域學程洞穴',
                                text='跨域學程洞穴'
                               ),
                                MessageTemplateAction(  #顯示文字計息
                                label='第二專長小溪',
                                text='第二專長小溪'
                               ),
                                MessageTemplateAction(  #顯示文字計息
                                label='我目前選不出來',
                                text='我目前選不出來'
                               )
                     
                            ]
                          )
                        )
                      ]
                    line_bot_api.reply_message(event.reply_token,message)
            
                    if mtext == '先等等':
                        func.先不用(event)
                    if mtext == '出發囉':
                        
                        func.提供關鍵詞(event)
                        x+=1
                    
                    if mtext == '好呀！':
                        func.提供關鍵詞(event)
                        x+=1
                    
                    if mtext == '先不用':
                       line_bot_api.reply_message(event.reply_token,TextSendMessage(text='希望這些推薦能幫你找到合胃口的跨領域紅蘿蔔！\n謝謝你願意和我聊天當朋友，若你想了解更多跨域森林或各個蘿蔔坑的資訊，可以在下方的選單找森林裡的其他朋友了解相關功能喔！\n隨時歡迎你呼喊我的名字「小圖」，回來找我聊天喔～')) 
                        

                    
                    if mtext == '雙修輔系灌木叢' or '跨域學程洞穴' or '第二專長小溪' or '我目前選不出來' :
                        subject_ans = func.subject(text_intersection)
                        rows = func.arrange_data('number1.csv') 
                        
                        holand_ans = func.return_course(func.get_quiz_results(stu_id_intersection,rows))
                        output=func.get_connection(subject_ans,holand_ans)
                        
                        message = [  #串列
                                TextSendMessage(  
                                text = '這樣啊！希望這個推薦對你有幫助...'
                                ), 
                                time.sleep(3),
                                TextSendMessage(  
                                text = '快看！前面就是校務資料中心大榕樹了，我經常把樹洞裡的UCAN測驗果實和跨域紅蘿蔔配在一起享用，迸出同時符合發展目標和興趣的跨域簡餐，讓我們一起來試試吧！'
                                ), 
                                TextSendMessage(  
                                text = "為了找到你在校務資料中心樹洞裡的測驗果實，請輸入你的學號～"
                                )
                              ]
          
                        line_bot_api.reply_message(event.reply_token,message)     
    
                
                    if mtext in student_id:
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
                                time.sleep(5),
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
                    elif output=='':
                        message = [  #串列
                                TextSendMessage(  
                                text = '但我試吃了一下你的跨域簡餐，發現這兩個味道相差太大了，實在不能配在一起享用，因此無法提供給你，很抱歉！'
                                ), 
                                time.sleep(2),
                                TextSendMessage( 
                                text = holand_ans
                                ),
                                time.sleep(5),
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
                    else:
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='感謝你！\n但很抱歉，樹洞裡找不到與你學號相對應的測驗果實，因此無法製作跨域簡餐(◞‸◟)')) 
                        
                        
                        
                        
                        
                       
                            
                        
                        
                  
            
                  

















                   

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
