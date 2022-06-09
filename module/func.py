from django.conf import settings

from linebot import LineBotApi

from linebot.models import TextSendMessage,ImageSendMessage
from pathlib import Path

from linebot.models import TemplateSendMessage, MessageTemplateAction, ButtonsTemplate,ConfirmTemplate, PostbackTemplateAction,PostbackAction
from linebot.models import ImagemapSendMessage, BaseSize, ImagemapAction, ImagemapArea, MessageImagemapAction, URIImagemapAction
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen
import os
import pandas as pd
import csv
import numpy as np
import time


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
BASE_DIR = Path(__file__).resolve().parent.parent

def begin(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  
            text = "叮咚叮！答對了\n歡迎進入森林～"
            ), 
            TextSendMessage(  
            text = "小圖是你的森林嚮導，我會盡全力地向你推薦雙修輔系灌木、跨域學程草原和第二專長小溪中，可能符合你發展目標或興趣的跨域蘿蔔坑！"
            ), 
            ImageSendMessage(
            original_content_url='https://imgur.com/VD1uuvm.png',
            preview_image_url='https://imgur.com/VD1uuvm.png'
            ),
            ImageSendMessage(
            original_content_url='https://imgur.com/nHVect4.png',
            preview_image_url='https://imgur.com/nHVect4.png'
            ),
            TemplateSendMessage(
            alt_text='準備好一起探索這座森林了嗎？',
            template=ConfirmTemplate(
                text='準備好一起探索這座森林了嗎？',  #主標題
                actions=[    
                   MessageTemplateAction(  
                         label='出發囉', #按鈕文字
                         text='出發囉' #顯示文字計息  
                   ),
                    MessageTemplateAction(  #顯示文字計息
                        label='先等等',
                        text='先等等'
                        )
                     
                ]
            )
          )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
        print (mtext)
        
def 先不用(event): 
    try:
        message = [
        TextSendMessage(
        text='(T▽T) 有甚麼問題想問我嗎～還是你目前不想要尋找蘿蔔坑呢？歡迎你透過以下連結到表單內留言給小圖哦！\n https://forms.gle/P6d5bkAzjy31tLSp8'
        ),
        TextSendMessage(  
        text = "當你準備好探索森林時，歡迎隨時呼喊我的名字「小圖」，回來找我一起玩喔~"
        )
    ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
        

def 提供關鍵詞(event):  
    try:
        message = [  #串列
            TextSendMessage(  
            text = "٩(●ᴗ●)۶ 好的，那麼我們進入森林吧～"
             ),
            TextSendMessage(  
            text = "我蒐集了許多跨域紅蘿蔔，快來選出三個符合你想發展的領域或有興趣的跨領域紅蘿蔔，讓我為你推薦蘿蔔坑吧～"
             ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/pqVJAli.png",
            alt_text='image 1',
            base_size=BaseSize(width=1040, height=650),
      
       actions = [
       MessageImagemapAction(
            text='中文',
            area=ImagemapArea(
                x=49, y=52, width=160, height=70
               )
            ),
        MessageImagemapAction(
            text='創意/創作',
            area=ImagemapArea(
                x=53, y=154, width=160, height=70
              )
            ),
        MessageImagemapAction(
             text='人文',
            area=ImagemapArea(
                x=49, y=258, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經典',
            area=ImagemapArea(
                x=52, y=360, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='歷史',
            area=ImagemapArea(
                x=51, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='文化',
            area=ImagemapArea(
                x=43, y=555, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='東亞',
            area=ImagemapArea(
                x=235, y=350, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='人權',
            area=ImagemapArea(
                x=249, y=553, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='中國',
            area=ImagemapArea(
                x=247, y=457, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='台灣',
            area=ImagemapArea(
                x=246, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='在地',
            area=ImagemapArea(
                x=246, y=154, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='幸福',
            area=ImagemapArea(
                x=248, y=54, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社會',
            area=ImagemapArea(
                x=441, y=149, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='非營利組織',
            area=ImagemapArea(
                x=440, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='公共治理',
            area=ImagemapArea(
                x=439, y=352, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社工',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='高齡',
            area=ImagemapArea(
                x=438, y=541, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='健康生活',
            area=ImagemapArea(
                x=628, y=59, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='美學',
            area=ImagemapArea(
                x=832, y=47, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='音樂',
            area=ImagemapArea(
                x=639, y=540, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='推理',
            area=ImagemapArea(
                x=641, y=459, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='哲學',
            area=ImagemapArea(
                x=635, y=351, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='外交領事',
            area=ImagemapArea(
                x=634, y=251, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='法律',
            area=ImagemapArea(
                x=635, y=148, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='英文',
            area=ImagemapArea(
                x=831, y=152, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='韓文',
            area=ImagemapArea(
                x=834, y=258, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='日文',
            area=ImagemapArea(
                x=833, y=357, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='德文',
            area=ImagemapArea(
                x=837, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='翻譯',
            area=ImagemapArea(
                x=840, y=546, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='政治',
            area=ImagemapArea(
                x=442, y=48, width=160, height=70
            )
           )
         ],
        ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/D87WWaX.png",
            alt_text='關鍵詞表2',
      base_size=BaseSize(width=1040, height=650),
      actions=[
        MessageImagemapAction(
            text='全英語',
            area=ImagemapArea(
                x=43, y=51, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='心理',
            area=ImagemapArea(
                x=45, y=164, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='行為',
            area=ImagemapArea(
                x=48, y=261, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='微生物',
            area=ImagemapArea(
                x=48, y=361, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='化學',
            area=ImagemapArea(
                x=47, y=453, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='物理',
            area=ImagemapArea(
                x=49, y=555, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='科技',
            area=ImagemapArea(
                x=245, y=559, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='資科',
            area=ImagemapArea(
                x=239, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='分析',
            area=ImagemapArea(
                x=235, y=353, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='線性代數',
            area=ImagemapArea(
                x=244, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='數學',
            area=ImagemapArea(
                x=244, y=159, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='創新',
            area=ImagemapArea(
                x=246, y=52, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='資管',
            area=ImagemapArea(
                x=443, y=52, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='領導',
            area=ImagemapArea(
                x=441, y=144, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='決策',
            area=ImagemapArea(
                x=444, y=251, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='管理',
            area=ImagemapArea(
                x=439, y=348, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='企管',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='永續',
            area=ImagemapArea(
                x=435, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='財精',
            area=ImagemapArea(
                x=635, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經濟',
            area=ImagemapArea(
                x=633, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='影視',
            area=ImagemapArea(
                x=635, y=345, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='行銷',
            area=ImagemapArea(
                x=630, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經營',
            area=ImagemapArea(
                x=633, y=151, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='國貿',
            area=ImagemapArea(
                x=626, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='理財',
            area=ImagemapArea(
                x=833, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='財經',
            area=ImagemapArea(
                x=839, y=153, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='會計',
            area=ImagemapArea(
                x=833, y=256, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='商務',
            area=ImagemapArea(
                x=830, y=356, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行政',
            area=ImagemapArea(
                x=834, y=451, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='地政/地產',
            area=ImagemapArea(
                x=834, y=548, width=160, height=70
                     )
                )

            ]
        )
    ]   
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def 小圖(event):  
    try:
        message = [  #串列
            TextSendMessage(  
            text = "我蒐集了許多跨域紅蘿蔔，快來選出三個符合你想發展的領域或有興趣的跨領域紅蘿蔔，讓我為你推薦蘿蔔坑吧～"
             ),
             ImagemapSendMessage(
            base_url= "https://imgur.com/pqVJAli.png",
            alt_text='image 1',
            base_size=BaseSize(width=1040, height=650),
      
       actions = [
       MessageImagemapAction(
            text='中文',
            area=ImagemapArea(
                x=49, y=52, width=160, height=70
               )
            ),
        MessageImagemapAction(
            text='創意/創作',
            area=ImagemapArea(
                x=53, y=154, width=160, height=70
              )
            ),
        MessageImagemapAction(
             text='人文',
            area=ImagemapArea(
                x=49, y=258, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經典',
            area=ImagemapArea(
                x=52, y=360, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='歷史',
            area=ImagemapArea(
                x=51, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='文化',
            area=ImagemapArea(
                x=43, y=555, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='東亞',
            area=ImagemapArea(
                x=235, y=350, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='人權',
            area=ImagemapArea(
                x=249, y=553, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='中國',
            area=ImagemapArea(
                x=247, y=457, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='台灣',
            area=ImagemapArea(
                x=246, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='在地',
            area=ImagemapArea(
                x=246, y=154, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='幸福',
            area=ImagemapArea(
                x=248, y=54, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社會',
            area=ImagemapArea(
                x=441, y=149, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='非營利組織',
            area=ImagemapArea(
                x=440, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='公共治理',
            area=ImagemapArea(
                x=439, y=352, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社工',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='高齡',
            area=ImagemapArea(
                x=438, y=541, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='健康生活',
            area=ImagemapArea(
                x=628, y=59, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='美學',
            area=ImagemapArea(
                x=832, y=47, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='音樂',
            area=ImagemapArea(
                x=639, y=540, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='推理',
            area=ImagemapArea(
                x=641, y=459, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='哲學',
            area=ImagemapArea(
                x=635, y=351, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='外交領事',
            area=ImagemapArea(
                x=634, y=251, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='法律',
            area=ImagemapArea(
                x=635, y=148, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='英文',
            area=ImagemapArea(
                x=831, y=152, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='韓文',
            area=ImagemapArea(
                x=834, y=258, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='日文',
            area=ImagemapArea(
                x=833, y=357, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='德文',
            area=ImagemapArea(
                x=837, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='翻譯',
            area=ImagemapArea(
                x=840, y=546, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='政治',
            area=ImagemapArea(
                x=442, y=48, width=160, height=70
            )
           )
         ],
        ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/D87WWaX.png",
            alt_text='關鍵詞表2',
      base_size=BaseSize(width=1040, height=650),
      actions=[
        MessageImagemapAction(
            text='全英語',
            area=ImagemapArea(
                x=43, y=51, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='心理',
            area=ImagemapArea(
                x=45, y=164, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='行為',
            area=ImagemapArea(
                x=48, y=261, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='微生物',
            area=ImagemapArea(
                x=48, y=361, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='化學',
            area=ImagemapArea(
                x=47, y=453, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='物理',
            area=ImagemapArea(
                x=49, y=555, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='科技',
            area=ImagemapArea(
                x=245, y=559, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='資科',
            area=ImagemapArea(
                x=239, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='分析',
            area=ImagemapArea(
                x=235, y=353, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='線性代數',
            area=ImagemapArea(
                x=244, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='數學',
            area=ImagemapArea(
                x=244, y=159, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='創新',
            area=ImagemapArea(
                x=246, y=52, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='資管',
            area=ImagemapArea(
                x=443, y=52, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='領導',
            area=ImagemapArea(
                x=441, y=144, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='決策',
            area=ImagemapArea(
                x=444, y=251, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='管理',
            area=ImagemapArea(
                x=439, y=348, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='企管',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='永續',
            area=ImagemapArea(
                x=435, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='財精',
            area=ImagemapArea(
                x=635, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經濟',
            area=ImagemapArea(
                x=633, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='影視',
            area=ImagemapArea(
                x=635, y=345, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='行銷',
            area=ImagemapArea(
                x=630, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經營',
            area=ImagemapArea(
                x=633, y=151, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='國貿',
            area=ImagemapArea(
                x=626, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='理財',
            area=ImagemapArea(
                x=833, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='財經',
            area=ImagemapArea(
                x=839, y=153, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='會計',
            area=ImagemapArea(
                x=833, y=256, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='商務',
            area=ImagemapArea(
                x=830, y=356, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行政',
            area=ImagemapArea(
                x=834, y=451, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='地政/地產',
            area=ImagemapArea(
                x=834, y=548, width=160, height=70
                     )
                )

            ]
        )
    ]   
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def 關鍵字結果(event):
    try:
        message = [  #串列
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
            label='跨域學程草原',
            text='跨域學程草原'
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
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def 輸學號(event): 
    try:
        message = [  #串列
        TextSendMessage(  
        text = '這樣啊！希望這個推薦對你有幫助...'
        ), 
        TextSendMessage(  
        text = '快看！前面就是校務資料中心大榕樹了，「職涯測驗地圖」就在裡面，它可以帶領我們找到職涯測驗結果和紅蘿蔔的跨域交集，讓我們一起來試試吧！'
        ), 
        TextSendMessage(  
        text = "為了解鎖你入學時做過的職涯興趣測驗結果，請輸入你的學號～"
        )
    ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

        
def subject(data,array):
    keyword, deparment, cross_field, second_specialty=data["關鍵字"].tolist(), data["科系"].tolist(), data["跨領域"].tolist(), data["第二專長"].tolist()
    
    data_dict={}
    for i in range(len(keyword)):
        data_dict[keyword[i]] = [ [deparment[i]] , [cross_field[i]] , [second_specialty[i]] ]
        
    derpar=[]
    cross_f=[]
    second_spe=[]

    for item in array:
        tem=data_dict[item]
        for i in range(3):
           # print((tem[i]))
          #  print(len(tem[i]))
            splited_text=str(tem[i][0]).split("、")
            if i==0:
                    #splited_text=(tem[i][0]).split("、")
                    for number_content in range(len(splited_text)):
                        derpar.append(splited_text[number_content])
            
            elif i==1:
               # splited_text=(tem[i][0]).split("、")
                for number_content in range(len(splited_text)):
                    if str(splited_text[number_content]) != "nan":
                        cross_f.append(splited_text[number_content])
                    
            else:
               # splited_text=(tem[i][0]).split("、")
                for number_content in range(len(splited_text)):
                    if str(splited_text[number_content]) != "nan":
                        second_spe.append(splited_text[number_content])

    # elimate repeated text
    derpar, cross_f, second_spe = list(set(derpar)), list(set(cross_f)), list(set(second_spe))
    
    text_1="🌳雙輔系灌木叢："
    text_2="🏕跨域學程草原："
    text_3="🏞第二專長小溪："

    for i in range(len(derpar)):
        if i==0:
            text_1+=derpar[i]
        else:
            text_1 = text_1+"，"+derpar[i]
            
    if len(cross_f) >= 1:
        for i in range(len(cross_f)):
            if i==0:
                text_2+=cross_f[i]
            else:
                text_2 = text_2+"，"+cross_f[i]

    else:
        pass
    if len(second_spe) >= 1:
        for i in range(len(second_spe)):
            if i==0:
                text_3+=second_spe[i]
            else:
                text_3 = text_3+"，"+second_spe[i]

    else:
        pass
    
    text = '有了！原來適合你的蘿蔔坑在這裡啊！\n ⚠️（以下隨機排序）⚠️'+"\n"+"\n"+ text_1 +"\n"+ text_2 +"\n"+text_3
    
    return text
    





def arrange_data(file):
  rows = {}
  with open(file, "r", encoding="utf-8") as fp:
    csvreader = csv.reader(fp)
    header = next(csvreader)
    for row in csvreader:
      rows[row[0]]=row[1]
  return rows

def get_quiz_results(number,rows):
  if len(rows.get(number)) > 5:
    return rows.get(number)[:5]
  elif len(rows.get(number)) <= 5:
    return rows.get(number)

def arrange_holland(file):
  second_specialty_rows = {}
  cross_domain_rows = {}
  auxiliary_department_rows = {}
  double_major_rows = {}
  with open(file, "r", encoding="utf-8") as fp:
    csvreader = csv.reader(fp)
    header = next(csvreader)
    for row in csvreader:
      second_specialty_rows[row[0]]=row[1]
      cross_domain_rows[row[2]]=row[3]
      auxiliary_department_rows[row[4]]=row[5]
      double_major_rows[row[6]]=row[7]
  second_specialty_rows = { k: v for k, v in second_specialty_rows.items() if v and v.strip()}
  cross_domain_rows = { k: v for k, v in cross_domain_rows.items() if v and v.strip()}
  auxiliary_department_rows = { k: v for k, v in auxiliary_department_rows.items() if v and v.strip()}
  double_major_rows = { k: v for k, v in double_major_rows.items() if v and v.strip()}

  return second_specialty_rows,cross_domain_rows,auxiliary_department_rows,double_major_rows

sec_spec_rows,cro_dom_rows,aux_dep_rows,dou_maj_rows = arrange_holland(BASE_DIR /'Holland .csv')

def return_course(holland_code):
  sec_spec = '🏞第二專長小溪：'
  cro_dom = '🏕跨域學程草原：'
  aux_dep = '輔系：'
  dou_maj = '🌳雙輔系灌木叢：'

  if len(holland_code) == 5:
    # 第二專長
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    if len(sec_spec) > 8:
      sec_spec = sec_spec[:-2]
    else:
      for key, value in sec_spec_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:3]) == 0:
          sec_spec = sec_spec + key + ', '
      if len(sec_spec) > 8:
        sec_spec = sec_spec[:-2]
      else:
        for key, value in sec_spec_rows.items():
          value = value.replace(" ","")
          if value.find(holland_code[:1]) == 0:
            sec_spec = sec_spec + key + ', '
        if len(sec_spec) > 8:
          sec_spec = sec_spec[:-2]
    # 跨領域學分學程
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    if len(cro_dom) > 8:
      cro_dom = cro_dom[:-2]
    else:
      for key, value in cro_dom_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:3]) == 0:
          cro_dom = cro_dom + key + ', '
      if len(cro_dom) > 8:
        cro_dom = cro_dom[:-2]
      else:
        for key, value in cro_dom_rows.items():
          value = value.replace(" ","")
          if value.find(holland_code[:1]) == 0:
            cro_dom = cro_dom + key + ', '
        if len(cro_dom) > 8:
          cro_dom = cro_dom[:-2]
    # 輔系
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    if len(aux_dep) > 7:
      aux_dep = aux_dep[:-2]
    else:
      for key, value in aux_dep_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:3]) == 0:
          aux_dep = aux_dep + key + ', '
      if len(aux_dep) > 7:
        aux_dep = aux_dep[:-2]
      else:
        for key, value in aux_dep_rows.items():
          value = value.replace(" ","")
          if value.find(holland_code[:1]) == 0:
            aux_dep = aux_dep + key + ', '
        if len(aux_dep) > 7:
          aux_dep = aux_dep[:-2]
    # 雙主修
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    if len(dou_maj) > 8:
      dou_maj = dou_maj[:-2]
    else:
      for key, value in dou_maj_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:3]) == 0:
          dou_maj = dou_maj + key + ', '
      if len(dou_maj) > 8:
        dou_maj = dou_maj[:-2]
      else:
        for key, value in dou_maj_rows.items():
          value = value.replace(" ","")
          if value.find(holland_code[:1]) == 0:
            dou_maj = dou_maj + key + ', '
        if len(dou_maj) > 8:
          dou_maj = dou_maj[:-2]
  if len(holland_code) == 3:
    # 第二專長
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    if len(sec_spec) > 8:
      sec_spec = sec_spec[:-2]
    else:
      for key, value in sec_spec_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          sec_spec = sec_spec + key + ', '
      if len(sec_spec) > 8:
        sec_spec = sec_spec[:-2]
    # 跨領域學分學程
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    if len(cro_dom) > 8:
      cro_dom = cro_dom[:-2]
    else:
      for key, value in cro_dom_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          cro_dom = cro_dom + key + ', '
      if len(cro_dom) > 8:
        cro_dom = cro_dom[:-2]
    # 輔系
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    if len(aux_dep) > 7:
      aux_dep = aux_dep[:-2]
    else:
      for key, value in aux_dep_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          aux_dep = aux_dep + key + ', '
      if len(aux_dep) > 7:
        aux_dep = aux_dep[:-2]
    # 雙主修
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    if len(dou_maj) > 8:
      dou_maj = dou_maj[:-2]
    else:
      for key, value in dou_maj_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          dou_maj = dou_maj + key + ', '
      if len(dou_maj) > 8:
        dou_maj = dou_maj[:-2]
  if len(holland_code) == 1:
    # 第二專長
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    if len(sec_spec) > 8:
      sec_spec = sec_spec[:-2]
    else:
      for key, value in sec_spec_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          sec_spec = sec_spec + key + ', '
      if len(sec_spec) > 8:
        sec_spec = sec_spec[:-2]
    # 跨領域學分學程
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    if len(cro_dom) > 8:
      cro_dom = cro_dom[:-2]
    else:
      for key, value in cro_dom_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          cro_dom = cro_dom + key + ', '
      if len(cro_dom) > 8:
        cro_dom = cro_dom[:-2]
    # 輔系
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    if len(aux_dep) > 8:
      aux_dep = aux_dep[:-2]
    else:
      for key, value in aux_dep_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          aux_dep = aux_dep + key + ', '
      if len(aux_dep) > 8:
        aux_dep = aux_dep[:-2]
    # 雙主修
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    if len(dou_maj) > 8:
      dou_maj = dou_maj[:-2]
    else:
      for key, value in dou_maj_rows.items():
        value = value.replace(" ","")
        if value.find(holland_code[:1]) == 0:
          dou_maj = dou_maj + key + ', '
      if len(dou_maj) > 8:
        dou_maj = dou_maj[:-2]
  return '謝謝！找到你的測驗地圖了~\n不過地圖涵蓋的蘿蔔坑與你所選的跨域紅蘿蔔沒有交集耶...\n但是單獨根據你的測驗結果，我還是可以為你推薦以下幾個職涯地圖上出現的蘿蔔坑：\n⚠️（以下隨機排序）⚠️'+'\n'+'\n' +dou_maj + '\n' + cro_dom + '\n' + sec_spec

def get_connection(subject_ans,holand_ans):
    subject_ans = subject_ans.replace(' ','').replace('：',':')
    holand_ans = holand_ans.replace(' ','').replace('：',':')

    pre_subject_ans= subject_ans.split('\n')
    pre_holand_ans= holand_ans.split('\n')

  # 雙輔系灌木叢
    aux_dep = []
  # 第二專長小溪
    sec_spec = []
  # 跨域學程洞穴
    cro_dom = []

    for item in pre_subject_ans:
      if '雙輔系灌木叢' in item:
        for i in item[7:].split(','):
          aux_dep.append(i)
      elif '第二專長小溪' in item:
        for i in item[7:].split(','):
          sec_spec.append(i)
      elif '跨域學程草原' in item:
        for i in item[7:].split(','):
          cro_dom.append(i)
    for item in pre_holand_ans:
      if '雙輔系灌木叢' in item:
        for i in item[7:].split(','):
          aux_dep.append(i)
      elif '第二專長小溪' in item:
        for i in item[7:].split(','):
          sec_spec.append(i)
      elif '跨域學程草原' in item:
        for i in item[7:].split(','):
          cro_dom.append(i)

    aux_dep = [i for i in aux_dep if i != '']
    sec_spec = [i for i in sec_spec if i != '']
    cro_dom = [i for i in cro_dom if i != '']
 
    aux = '🌳雙輔系灌木叢：'
    sec = '🏞第二專長小溪：'
    cro = '🏕跨域學程草原：'
    if list(unique_everseen(duplicates(aux_dep))) != []:
      aux += list(unique_everseen(duplicates(aux_dep)))[0]
    if list(unique_everseen(duplicates(sec_spec))) != []:
      sec += list(unique_everseen(duplicates(sec_spec)))[0]
    if list(unique_everseen(duplicates(cro_dom))) != []:
      cro += list(unique_everseen(duplicates(cro_dom)))[0]
    
    if (aux.split('：')[1] != '') or (sec.split('：')[1] != '') or (cro.split('：')[1] != ''):
        return '有了！跟著地圖的軌跡走...\nDo Re Mi So～\n跨域交集出爐囉，蘿蔔坑在這裡：\n⚠️（以下隨機排序）⚠️\n' + '\n'+ aux + '\n' + cro + '\n' + sec
    else:
        return ''

def 錯誤訊息(event):  
    try:
        message = [  #串列
            TemplateSendMessage(
            alt_text='發生錯誤',
            template=ButtonsTemplate(
            title='(◞‸◟) 登愣！',
            text='如輸入錯誤，可直接重新輸入；確定輸入無誤，請告訴小圖你的座標位置',  #主標題
            actions=[    
            MessageTemplateAction(  
            label='我在「通關密語」', #按鈕文字
            text='我在「通關密語」' #顯示文字計息  
            ),
            MessageTemplateAction(  #顯示文字計息
            label='我在「輸入學號」找果實',
            text='我在「輸入學號」找果實'
            ),
            MessageTemplateAction(  
            label='我不知道我在哪', #按鈕文字
            text='我不知道我在哪' #顯示文字計息  
            )
                     
           ]
         )
        )
    ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))

def 聯絡人資訊(event):  
    try:
        message = [  #串列
            TextSendMessage(  
            text = "請點選你要查詢的跨領域學習承辦單位～"
            ),        
            ImagemapSendMessage(
            base_url= "https://imgur.com/SCqhhaM.png",
            alt_text='雙輔系聯絡人',
            base_size=BaseSize(width=1040, height=650),
      
            actions = [
               URIImagemapAction(
               link_uri='https://web-ch.scu.edu.tw/chinese/dept_member/3374',
                area=ImagemapArea(
                   x=12, y=125, width=160, height=70
                  
                )
               ),
        URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/index.php/history/teacher_resume/5234',
            area=ImagemapArea(
                x=226, y=109, width=160, height=70
              )
            ),
        URIImagemapAction(
             link_uri='https://web-ch.scu.edu.tw/philos/dept_member/5986',
            area=ImagemapArea(
                x=445, y=117, width=160, height=70
                )
            ),
        URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/index.php/politics/dept_member/7895',
            area=ImagemapArea(
                x=667, y=109, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/society/dept_member/375',
            area=ImagemapArea(
                x=867, y=107, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/sw/dept_member/3535',
            area=ImagemapArea(
                x=6, y=234, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='http://english.scu.edu.tw/?page_id=2267',
            area=ImagemapArea(
                x=246, y=230, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/japanese/dept_member/3883',
            area=ImagemapArea(
                x=449, y=230, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/deutsch/staff/6037',
            area=ImagemapArea(
                x=663, y=238, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/math/dept_member/561',
            area=ImagemapArea(
                x=875, y=226, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='http://www.phys.scu.edu.tw/index.php/zh-tw/page-menuitem-staff-assistant',
            area=ImagemapArea(
                x=18, y=339, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/chem/dept_member/11459',
            area=ImagemapArea(
                x=248, y=331, width=160, height=70
                )
            ),
        URIImagemapAction(
            link_uri='https://microbiology.scu.edu.tw/nexus/content/%E7%B3%BB%E8%BE%A6%E5%85%AC%E5%AE%A4',
            area=ImagemapArea(
                x=453, y=333, width=160, height=70
               
              )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/index.php/psy/dept_member/3986',
            area=ImagemapArea(
                x=665, y=349, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/index.php/law/staff/5357',
            area=ImagemapArea(
                x=881, y=345, width=160, height=70   
               )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/econ/dept_member/5274',
            area=ImagemapArea(
                x=18, y=456, width=160, height=70
              )
            ),
          URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/acc/dept_member/4226',
            area=ImagemapArea(
                x=238, y=439, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://www.ba.scu.edu.tw/zh-hant/administration',
            area=ImagemapArea(
                x=435, y=443, width=160, height=70
          )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/index.php/ibsu/web_page/12009',
            area=ImagemapArea(
                x=669, y=443, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://www.feam.scu.edu.tw/faculty/6',
            area=ImagemapArea(
                x=863, y=435, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='http://www.csim.scu.edu.tw/teacher_list.aspx?c=TEACHER&cid=3',
            area=ImagemapArea(
                x=112, y=562, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://web-ch.scu.edu.tw/music/dept_member/3615',
            area=ImagemapArea(
                x=424, y=550, width=160, height=70
                )
            ),
         URIImagemapAction(
            link_uri='https://bigdata.scu.edu.tw/team/#executive-lineup',
            area=ImagemapArea(
                x=729, y=554, width=160, height=70
        
               
                )
            )            
               
         ],
        ),    
         ImagemapSendMessage(
        base_url= "https://imgur.com/jIeei8k.png",
        alt_text='學程＆第二專長聯絡人',
        base_size=BaseSize(width=1040, height=650),
      
       actions = [
       MessageImagemapAction(
            text='聯絡人：黃炫榕 助理\nE-mail：pcci@gm.scu.edu.tw 電話：02-2881 9471＃6104 辦公室：111台北市士林區臨溪路70號 第二教研大樓十樓D1007室 http://www.scu.edu.tw/pcci/',
            area=ImagemapArea(
                x=198, y=109, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：黃炫榕 助理\nE-mail：pcci@gm.scu.edu.tw\n電話：02-2881 9471＃6104\n辦公室：111台北市士林區臨溪路70號 第二教研大樓十樓D1007室\nhttp://www.scu.edu.tw/pcci/',
            area=ImagemapArea(
                x=18, y=111, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：熊賢芝 秘書\nE-mail：hchsiung@scu.edu.tw\n電話：02-2881 9471＃6102\nhttps://web-ch.scu.edu.tw/artsoc/web_page/8635',
            area=ImagemapArea(
                x=353, y=120, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：黃依晴 助教\n電話：02-2881 9471＃6951\nE-mail：yiching@scu.edu.tw\nhttp://www.hrp.scu.edu.tw/aboutUs/staff/%E8%A1%8C%E6%94%BF%E4%BA%BA%E5%93%A1%E4%BB%8B%E7%B4%B9',
            area=ImagemapArea(
                x=541, y=112, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：   \nE-mail ：ft@scu.edu.tw\n電話：02-2311 1531＃2891\n傳真電話：02-2311 6673\n辦公室：城中校區 鑄秋大樓一樓 2107室\n上班時間：星期一至五 上午8:00~12:00 下午1:00~5:00\nhttp://www.scu.edu.tw/ft',
            area=ImagemapArea(
                x=702, y=112, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：   \nE-mail ：ft@scu.edu.tw\n電話：02-2311 1531＃2891\n傳真電話：02-2311 6673\n辦公室：城中校區 鑄秋大樓一樓 2107室\n上班時間：星期一至五 上午8:00~12:00 下午1:00~5:00\nhttp://www.scu.edu.tw/ft',
            area=ImagemapArea(
                x=871, y=104, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：江怡靜\nE-mail ：yiching0701@scu.edu.tw\n電話：02-2311 1531＃2881\n辦公室 : 10048 台北市中正區貴陽街一段五十六號\nhttps://web-ch.scu.edu.tw/ife/dept_member/6734',
            area=ImagemapArea(
                x=33, y=240, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：江怡靜\nE-mail ：yiching0701@scu.edu.tw\n電話：02-2311 1531＃2881\n辦公室 : 10048 台北市中正區貴陽街一段五十六號\nhttps://web-ch.scu.edu.tw/ife/dept_member/6734',
            area=ImagemapArea(
                x=187, y=253, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=367, y=217, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=538, y=241, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=706, y=239, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=869, y=235, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=41, y=341, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳如玉\n電話：02-2881 9471＃6103',
            area=ImagemapArea(
                x=206, y=347, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：靶耐歐兒\n電話：02-2881 9471＃6133',
            area=ImagemapArea(
                x=373, y=345, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：靶耐歐兒\n電話：02-2881 9471＃6133',
            area=ImagemapArea(
                x=522, y=345, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：靶耐歐兒\n電話：02-2881 9471＃6133',
            area=ImagemapArea(
                x=691, y=351, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：張秀卿\n電話：02-2881 9471＃6173',
            area=ImagemapArea(
                x=867, y=352, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：楊雅惠\n電話：02-2881 9471＃6212',
            area=ImagemapArea(
                x=37, y=458, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：王姿惠\n電話：02-2881 9471＃6252',
            area=ImagemapArea(
                x=184, y=452, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：古政昕\n電話：02-2881 9471＃6302',
            area=ImagemapArea(
                x=369, y=462, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：歐孟芬\n電話：02-2881 9471＃6332',
            area=ImagemapArea(
                x=510, y=462, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：歐孟芬\n電話：02-2881 9471＃6332',
            area=ImagemapArea(
                x=687, y=462, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：施宜德\n電話：02-2881 9471＃6372',
            area=ImagemapArea(
                x=863, y=450, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：張怡\n電話：02-2881 9471＃6462',
            area=ImagemapArea(
                x=37, y=560, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：施璇姬\n電話：02-2881 9471＃6482',
            area=ImagemapArea(
                x=200, y=552, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：施璇姬\n電話：02-2881 9471＃6482',
            area=ImagemapArea(
                x=371, y=558, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：范清昉\n電話：02-2881 9471＃6522',
            area=ImagemapArea(
                x=544, y=552, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：范清昉\n電話：02-2881 9471＃6522',
            area=ImagemapArea(
                x=706, y=564, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：楊淑卿\n電話：02-2881 9471＃6562',
            area=ImagemapArea(
                x=859, y=552, width=140, height=90
            )
           )
         ],
        ),
            
       
            ImagemapSendMessage(
            base_url= "https://imgur.com/qfGPhgw.png",
            alt_text='第二專長聯絡人',
             base_size=BaseSize(width=1040, height=650),
      
       actions = [
      MessageImagemapAction(
            text='聯絡人：劉紋伶\n電話：02-2881 9471＃6652',
            area=ImagemapArea(
                x=37, y=120, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：任士芬\n電話：02-2881 9471＃6682',
            area=ImagemapArea(
                x=201, y=125, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：徐小燕\n電話：02-2881 9471＃6732',
            area=ImagemapArea(
                x=387, y=125, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：黃慧琴\n電話：02-2881 9471＃6782',
            area=ImagemapArea(
                x=533, y=112, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：李瑞梅\n電話：02-2881 9471＃6842',
            area=ImagemapArea(
                x=698, y=126, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林淑靜\n電話：02-2881 9471＃6892',
            area=ImagemapArea(
                x=871, y=120, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林淑靜\n電話：02-2881 9471＃6892',
            area=ImagemapArea(
                x=26, y=219, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：郭葉瑋\n電話：02-2311 1531＃2511',
            area=ImagemapArea(
                x=204, y=230, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：郭葉瑋\n電話：02-2311 1531＃25113',
            area=ImagemapArea(
                x=367, y=217, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：郭葉瑋\n電話：02-2311 1531＃2511',
            area=ImagemapArea(
                x=538, y=241, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：郭葉瑋\n電話：02-2311 1531＃25113',
            area=ImagemapArea(
                x=706, y=239, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：郭葉瑋\n電話：02-2311 1531＃2511',
            area=ImagemapArea(
                x=869, y=235, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳玟君\n電話：02-2311 1531＃2891',
            area=ImagemapArea(
                x=28, y=341, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=206, y=347, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=373, y=345, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=522, y=345, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=691, y=351, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=867, y=352, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：林欣君\n電話：02-2311 1531＃2923',
            area=ImagemapArea(
                x=37, y=458, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：鄒淑芳\n電話：02-2311 1531＃2661',
            area=ImagemapArea(
                x=184, y=452, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：鄒淑芳\n電話：02-2311 1531＃2661',
            area=ImagemapArea(
                x=348, y=449, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：邱敏惠\n電話：02-2311 1531＃2591',
            area=ImagemapArea(
                x=510, y=462, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：莊明琪\n電話：02-2311 1531＃2601',
            area=ImagemapArea(
                x=687, y=462, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：呂鴻玲\n電話：02-2311 1531＃2701',
            area=ImagemapArea(
                x=863, y=450, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：沈靜芝\n電話：02-2311 1531＃2621',
            area=ImagemapArea(
                x=31, y=540, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：李雪真\n電話：02-2311 1531＃2801',
            area=ImagemapArea(
                x=204, y=552, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳姿吟\n電話：02-2881 9471＃59352',
            area=ImagemapArea(
                x=366, y=459, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：陳姿吟\n電話：02-2881 9471＃5935',
            area=ImagemapArea(
                x=533, y=546, width=140, height=90
                )
            ),
        MessageImagemapAction(
            text='聯絡人：劉思怡\n電話：02-2881 9471＃6092',
            area=ImagemapArea(
                x=690, y=549, width=140, height=90
                )
            ),
        MessageImagemapAction(
             text='聯絡人：王治文\n電話： 02-2881 9471＃6463\nE-mail：amigo@scu.edu.tw',
            area=ImagemapArea(
                x=873, y=549, width=140, height=90
            )
           )
         ]
        )
    ]    
            
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def 應修課程(event): 
    try:
        message=TextSendMessage(
        text='◆查看「雙修輔系灌木」和「跨領域草原」應修課程：\n http://www.scu.edu.tw/~curr/p3-2cos.htm\n◇查看「第二專長小溪」應修課程:\n   https://web-ch.scu.edu.tw/regcurr/file/10477'
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def 申請條件(event): 
    try:
        message=TextSendMessage(
        text='◆查看「雙修輔系灌木」和「跨領域草原」申請條件：\n   https://api.sys.scu.edu.tw/academic/\n◇查看「第二專長小溪」申請條件:\n   https://web-ch.scu.edu.tw/regcurr/file/10477'
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def 本學期開課(event): 
    try:
        message=TextSendMessage(
        text='◆查看「雙修輔系灌木」和「跨領域草原」本學期開課：\n   https://web.sys.scu.edu.tw/class40.asp?option=1\n◇查看「第二專長小溪」本學期開課: \n   https://course.sys.scu.edu.tw/currlist/SecExpQueryCls.aspx'
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))






      
 
  

    
       


    
