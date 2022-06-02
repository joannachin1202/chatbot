# -*- coding: utf-8 -*-
"""
Created on Thu May 19 00:00:57 2022

@author: SCU
"""

from django.conf import settings
from pathlib import Path
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage , TextSendMessage, TemplateSendMessage, ConfirmTemplate, MessageTemplateAction, ButtonsTemplate, ImagemapSendMessage, BaseSize, ImagemapAction, ImagemapArea, MessageImagemapAction
from module import func


from linebot.models import PostbackEvent
from urllib.parse import parse_qsl
import time
import pandas as pd


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
BASE_DIR = Path(__file__).resolve().parent.parent

tem={}
check={}
main_word =['中文','歷史','哲學','政治','社會','社工','音樂','英文','日文','德文','數學','物理','化學','微生物','心理','法律'
,'經濟','會計','企管','國貿','財精','資管','資科','管理','經營','創意/創作','人文','非營利組織','東亞','全英語','人權','財經'
,'科技','中國','幸福','在地','創新','美學','經典','台灣','影視','永續','推理','領導','決策','分析','公共治理','韓文','文化'
,'翻譯','線性代數','健康生活','行為','高齡','外交領事','行政','商務','地政/地產','行銷','理財']

student_id=list(func.arrange_data(BASE_DIR /'number1.csv'))
rows = func.arrange_data(BASE_DIR /'number1.csv') 
data = pd.read_excel(BASE_DIR / 'Keywords.xlsx',sheet_name="關鍵詞表(推薦)")

@csrf_exempt
def callback(request):
    global check
    global tem
    global text
    global rows
    global main_word
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
                    user_id = event.source.user_id
                    
                    
                    if mtext == "兔子" or mtext == "兔" or mtext == "小兔" or mtext == '小兔子' or mtext =='rabbit': #希望調整成只要輸入任意文字都會回覆
                       func.begin(event) 
                     
                    elif mtext == '承辦人員資訊':
                         func.聯絡人資訊(event)
                    
                    elif mtext == '應修課程':
                         func.應修課程(event)
                         
                    elif mtext == '申請條件':
                         func.申請條件(event)
                    
                    elif mtext.startswith('聯絡人'):
                         line_bot_api.reply_message(event.reply_token,TextSendMessage(text='希望對你有幫助~'))
                    elif mtext == '本學期開課':
                         func.本學期開課(event)
            
                    
                    elif mtext == '好呀！' or mtext == '小圖':
                         func.小圖(event)
                         
                         if user_id not in check.keys():
                             check[user_id] = 0
                             check[user_id] += 1
                        
                         elif (user_id in check):
                            check[user_id] +=1
                        
                        
                    
                    elif mtext == '先不用':
                        message = [  #串列
                                 
                                 TextSendMessage( 
                                 text = '小圖的夢想是成為一名優秀的跨域森林嚮導，希望由小圖帶領過的你，能透過連結填寫表單，給予小圖鼓勵並幫助小圖成長！\n https://forms.gle/P6d5bkAzjy31tLSp8 '
                                 ),
                                 TextSendMessage( 
                                 text = '隨時歡迎你打字呼叫我的名字「小圖」,回來再選一次紅蘿蔔，一起探索森林更多樣貌喔～'
                                 )
                                ]
                        
                        line_bot_api.reply_message(event.reply_token,message)
                       
                    
                    elif mtext == '我在「通關密語」':
                       line_bot_api.reply_message(event.reply_token,TextSendMessage(text='小圖是一隻「兔子」呦！\n請你試試看在訊息欄打字發送「兔子」~')) 
                   
                    elif mtext == '我在「輸入學號」找果實':
                        del tem[user_id]
                        message = [  #串列
                                 TextSendMessage(  
                                 text = '感謝你！\n但很抱歉，樹洞裡沒有你的測驗果實，可能因為你沒有做過測驗，因此無法製作跨域簡餐 (⋟_⋞)'
                                 ),
                                 TextSendMessage( 
                                 text = '希望這些推薦能幫你找到合胃口的跨領域紅蘿蔔！\n謝謝你願意和我聊天當朋友,若你想更加了解跨域森林或各個蘿蔔坑,可以在下方的選單找森林裡的其他朋友了解相關資訊喔！'
                                 ),
                                 ImagemapSendMessage(
                                 base_url= "https://imgur.com/Qj0jpdi.png",
                                 alt_text='NPS',
                                 base_size=BaseSize(width=1040, height=650),
      
                                  actions = [
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：０／１０',
                                      area=ImagemapArea(
                                          x=0, y=339, width=174, height=153
                                          )
                                      ),
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：1／１０',
                                      area=ImagemapArea(
                                          x=176, y=338, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：2／１０',
                                      area=ImagemapArea(
                                          x=350, y=340, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：3／１０',
                                      area=ImagemapArea(
                                          x=524, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：4／１０',
                                      area=ImagemapArea(
                                          x=694, y=342, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：5／１０',
                                      area=ImagemapArea(
                                          x=870, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：6／１０',
                                      area=ImagemapArea(
                                          x=0, y=498, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：7／１０',
                                      area=ImagemapArea(
                                          x=210, y=496, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：8／１０',
                                      area=ImagemapArea(
                                          x=417, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：9／１０',
                                      area=ImagemapArea(
                                          x=623, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：10／１０',
                                      area=ImagemapArea(
                                          x=832, y=496, width=204, height=153
                                          )
                                      )
                                 ]
                                  )
                                 ]
                        line_bot_api.reply_message(event.reply_token,message)
                        
                    elif mtext.startswith('我會推薦'):
                         message = [  #串列
                                 TextSendMessage(  
                                 text =' 謝謝你的回覆，小圖會繼續努力的！'
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
                        
                    
                    elif mtext == '我不知道我在哪':
                       line_bot_api.reply_message(event.reply_token,TextSendMessage(text='走失了嗎？\n呼喊我的名字「小圖」，我會馬上把你帶回森林入口哦！\n\n還是你遇到困難或疑惑呢？\n透過以下連結到表單內留言給小圖發生了什麼事吧！\n\nhttps://forms.gle/P6d5bkAzjy31tLSp8')) 
                   #要看 tem 有多長用 len（）
                    # 當長度是三時我
                    elif user_id in check.keys() and check[user_id]==1:
                            
                        if mtext not in main_word:
                            # 輸入文字不是科目 會被提醒
                            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='請點選圖片中的紅蘿蔔喔！')) 
                        
                        if user_id in tem.keys() and mtext in main_word:
                            tem[user_id].append(mtext)
                        
                            
                        if user_id in tem.keys() and len(tem[user_id])==3:
                            content=func.subject(data,tem[user_id])
                            #关闭
                            check[user_id]-=1
                            #清除
                            message = [  #串列
                                TextSendMessage(  
                                text = 'yum yum～待我細細回想這滋味...'
                                ), 
                                TextSendMessage(  
                                text = content
                                ), 
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
                                  label='目前選不出來',
                                  text='目前選不出來'
                                  )
                                ]
                               )
                              )
                           ]

                            line_bot_api.reply_message(event.reply_token,message)
                        
                        elif (user_id not in tem.keys()) and (mtext in main_word):
                            tem[user_id] = []
                            #生成後加入文字
                            tem[user_id].append(mtext)
                        
            
                    elif mtext == '雙修輔系灌木叢':
                         func.輸學號(event)
                    elif mtext == '跨域學程洞穴':
                         func.輸學號(event)
                    elif mtext == '第二專長小溪':
                         func.輸學號(event)
                    elif mtext == '目前選不出來' :
                         func.輸學號(event)
                         
                    elif mtext == '先等等':
                        func.先不用(event)
                        
                    elif mtext == '出發囉':
                        func.提供關鍵詞(event)
                        if user_id not in check.keys():
                            check[user_id] = 0
                            check[user_id] += 1
                       
                        elif (user_id in check) and check[user_id]==0:
                           check[user_id] +=1
                    
                    elif mtext == '交集':
                        subject_ans = func.subject(data,tem[user_id])
                        
                        holand_ans = func.return_course(func.get_quiz_results(stu_id_intersection,rows))
                        output=func.get_connection(subject_ans,holand_ans)
                        line_bot_api.reply_message(event.reply_token,TextSendMessage(text=output))     
    
                
                    elif mtext in student_id:
                        stu_id_intersection = mtext

                        subject_ans = func.subject(data,tem[user_id])
                        holand_ans = func.return_course(func.get_quiz_results(stu_id_intersection,rows))
                        output=func.get_connection(subject_ans,holand_ans)
                        
                        if output== '' :
                           del tem[user_id] 
                           del check[user_id]
                           message = [  #串列
                                 TextSendMessage(  
                                 text = '但我試吃了一下你的跨域簡餐，發現這兩個味道相差太大了，實在不能配在一起享用，因此無法提供給你同時符合你挑選的紅蘿蔔和職涯測驗結果的推薦，很抱歉！'
                                 ), 
                                 TextSendMessage( 
                                 text = holand_ans
                                 ),
                                 TextSendMessage( 
                                 text = '希望這些推薦能幫你找到合胃口的跨領域紅蘿蔔！\n謝謝你願意和我聊天當朋友,若你想更加了解跨域森林或各個蘿蔔坑,可以在下方的選單找森林裡的其他朋友了解相關資訊喔！'
                                 ),
                                 ImagemapSendMessage(
                                 base_url= "https://imgur.com/Qj0jpdi.png",
                                 alt_text='NPS',
                                 base_size=BaseSize(width=1040, height=650),
      
                                  actions = [
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：０／１０',
                                      area=ImagemapArea(
                                          x=0, y=339, width=174, height=153
                                          )
                                      ),
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：1／１０',
                                      area=ImagemapArea(
                                          x=176, y=338, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：2／１０',
                                      area=ImagemapArea(
                                          x=350, y=340, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：3／１０',
                                      area=ImagemapArea(
                                          x=524, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：4／１０',
                                      area=ImagemapArea(
                                          x=694, y=342, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：5／１０',
                                      area=ImagemapArea(
                                          x=870, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：6／１０',
                                      area=ImagemapArea(
                                          x=0, y=498, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：7／１０',
                                      area=ImagemapArea(
                                          x=210, y=496, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：8／１０',
                                      area=ImagemapArea(
                                          x=417, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：9／１０',
                                      area=ImagemapArea(
                                          x=623, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：10／１０',
                                      area=ImagemapArea(
                                          x=832, y=496, width=204, height=153
                                          )
                                      )
                                 ]
                                  )
                                 ]
                           line_bot_api.reply_message(event.reply_token,message)
                           
                           
         

                            
                        else:  
                            
                            del tem[user_id] 
                            del check[user_id]
                            
                            message = [  #串列
                                TextSendMessage(  
                                text = '謝謝！找到你的測驗果實了～'
                                ), 
                                TextSendMessage( 
                                text = output
                                ),
                                TextSendMessage( 
                                 text = '希望這些推薦能幫你找到合胃口的跨領域紅蘿蔔！\n謝謝你願意和我聊天當朋友,若你想更加了解跨域森林或各個蘿蔔坑,可以在下方的選單找森林裡的其他朋友了解相關資訊喔！'
                                 ),
                                 ImagemapSendMessage(
                                 base_url= "https://imgur.com/Qj0jpdi.png",
                                 alt_text='NPS',
                                 base_size=BaseSize(width=1040, height=650),
      
                                  actions = [
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：０／１０',
                                      area=ImagemapArea(
                                          x=0, y=339, width=174, height=153
                                          )
                                      ),
                                  MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：1／１０',
                                      area=ImagemapArea(
                                          x=176, y=338, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：2／１０',
                                      area=ImagemapArea(
                                          x=350, y=340, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：3／１０',
                                      area=ImagemapArea(
                                          x=524, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：4／１０',
                                      area=ImagemapArea(
                                          x=694, y=342, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：5／１０',
                                      area=ImagemapArea(
                                          x=870, y=344, width=174, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：6／１０',
                                      area=ImagemapArea(
                                          x=0, y=498, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：7／１０',
                                      area=ImagemapArea(
                                          x=210, y=496, width=204, height=153
                                          )
                                      ),
                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：8／１０',
                                      area=ImagemapArea(
                                          x=417, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：9／１０',
                                      area=ImagemapArea(
                                          x=623, y=496, width=204, height=153
                                          )
                                      ),

                                 MessageImagemapAction(
                                      text='我會推薦「小圖同學」給朋友或同學的程度是：10／１０',
                                      area=ImagemapArea(
                                          x=832, y=496, width=204, height=153
                                          )
                                      )
                                 ]
                                  )
                                 ]
                            line_bot_api.reply_message(event.reply_token,message)
                    else:
                      func.錯誤訊息(event)
                        
                      
                       
                   
                  
            
                  

















                   

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
