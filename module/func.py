from django.conf import settings

from linebot import LineBotApi

from linebot.models import TextSendMessage


from linebot.models import TemplateSendMessage, MessageTemplateAction, ButtonsTemplate,ConfirmTemplate, PostbackTemplateAction,PostbackAction
from linebot.models import ImagemapSendMessage, BaseSize, ImagemapAction, ImagemapArea, MessageImagemapAction
import os
import pandas as pd
import csv
import numpy as np


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def begin(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  
            text = "我在這裡會盡我所能的推薦你適合的課程"
            ),            
           TemplateSendMessage(
            alt_text='確認是否推薦',
            template=ConfirmTemplate(
                text='想問你是不是需要我的推薦呢？',  #主標題
                actions=[    
                   MessageTemplateAction(  
                         label='想試試', #按鈕文字
                         text='想試試' #顯示文字計息  
                   ),
                    MessageTemplateAction(  #顯示文字計息
                        label='先不用',
                        text='先不用'
                        )
                     
                ]
            )
          )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def 先不用(event): 
    try:
        message = TextSendMessage(text='想請問你是不是有其他問題要問我') 
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
def 想試試(event): 
    try:
       message = TemplateSendMessage(
    alt_text='喜歡跨領域學習還是喜歡與自身所學相關',
    template=ButtonsTemplate(
        title='在開始之前，想要了解你喜歡跨領域學習還是喜歡與自身所學相關的呢?',
        text='請選擇',
        actions=[
            MessageTemplateAction(
                label='跨領域學習',
                text='跨領域學習'
            ),
            MessageTemplateAction(
                label='與自身所學相關',
                text='與自身所學相關'
            ),
        ]
    )
)
       line_bot_api.reply_message(event.reply_token,message)  
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        

def 提供關鍵詞(event):  
    try:
        message = [  #串列
            TextSendMessage(  
            text = "這樣我了解了！\n現在想要先請你從下方我提供的關鍵字當中挑選幾個你有興趣的，\n這可以幫助我知道你大概對什麼課程有興趣喔～"
             ), 
            TextSendMessage(  
            text = "在下面的兩張圖片裡，請你幫我在圖片上點選三個有興趣的關鍵詞"
             ),
            ImagemapSendMessage(
            base_url= "https://i.imgur.com/selXnPZ.png",
            alt_text='image 1',
             base_size=BaseSize(width=1040, height=650),
      
       actions = [
       MessageImagemapAction(
            text='中文',
            area=ImagemapArea(
                x=43, y=33, width=160, height=70
               )
            ),
        MessageImagemapAction(
            text='歷史',
            area=ImagemapArea(
                x=45, y=137, width=160, height=70
              )
            ),
        MessageImagemapAction(
             text='哲學',
            area=ImagemapArea(
                x=45, y=237, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='政治',
            area=ImagemapArea(
                x=40, y=330, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社會',
            area=ImagemapArea(
                x=40, y=420, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社工',
            area=ImagemapArea(
                x=43, y=532, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='化學',
            area=ImagemapArea(
                x=245, y=530, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='物理',
            area=ImagemapArea(
                x=239, y=426, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='數學',
            area=ImagemapArea(
                x=235, y=324, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='德文',
            area=ImagemapArea(
                x=244, y=235, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='日文',
            area=ImagemapArea(
                x=244, y=142, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='音樂',
            area=ImagemapArea(
                x=244, y=38, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='微生物',
            area=ImagemapArea(
                x=439, y=31, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='心理',
            area=ImagemapArea(
                x=439, y=127, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='法律',
            area=ImagemapArea(
                x=444, y=227, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='經濟',
            area=ImagemapArea(
                x=441, y=321, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='會計',
            area=ImagemapArea(
                x=443, y=420, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='企管',
            area=ImagemapArea(
                x=431, y=518, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='經營',
            area=ImagemapArea(
                x=633, y=518, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='管理',
            area=ImagemapArea(
                x=633, y=424, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='資科',
            area=ImagemapArea(
                x=633, y=328, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='資管',
            area=ImagemapArea(
                x=633, y=232, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='財精',
            area=ImagemapArea(
                x=633, y=132, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='國貿',
            area=ImagemapArea(
                x=633, y=36, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='創意',
            area=ImagemapArea(
                x=833, y=29, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='人文',
            area=ImagemapArea(
                x=833, y=130, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='非營利組織',
            area=ImagemapArea(
                x=833, y=230, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='東亞',
            area=ImagemapArea(
                x=833, y=330, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='全英語',
            area=ImagemapArea(
                x=833, y=430, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='人權',
            area=ImagemapArea(
                x=833, y=530, width=160, height=70
            )
           )
         ],
        ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/sFu1Hho.png",
            alt_text='關鍵詞表2',
      base_size=BaseSize(width=1040, height=650),
      actions=[
        MessageImagemapAction(
            text='財經',
            area=ImagemapArea(
                x=43, y=33, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='科技',
            area=ImagemapArea(
                x=45, y=137, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='中國',
            area=ImagemapArea(
                x=45, y=237, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='幸福',
            area=ImagemapArea(
                x=40, y=330, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='在地',
            area=ImagemapArea(
                x=40, y=420, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='創新',
            area=ImagemapArea(
                x=43, y=532, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='永續',
            area=ImagemapArea(
                x=245, y=530, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='影視',
            area=ImagemapArea(
                x=239, y=426, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='台灣',
            area=ImagemapArea(
                x=235, y=324, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='創作',
            area=ImagemapArea(
                x=244, y=235, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經典',
            area=ImagemapArea(
                x=244, y=142, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='美學',
            area=ImagemapArea(
                x=244, y=38, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='推理',
            area=ImagemapArea(
                x=439, y=31, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='領導',
            area=ImagemapArea(
                x=439, y=127, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='決策',
            area=ImagemapArea(
                x=444, y=227, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='分析',
            area=ImagemapArea(
                x=441, y=321, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='公共治理',
            area=ImagemapArea(
                x=443, y=420, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='韓文',
            area=ImagemapArea(
                x=431, y=518, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='高齡',
            area=ImagemapArea(
                x=633, y=518, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行為',
            area=ImagemapArea(
                x=633, y=424, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='健康生活',
            area=ImagemapArea(
                x=633, y=328, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='線性代數',
            area=ImagemapArea(
                x=633, y=232, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='翻譯',
            area=ImagemapArea(
                x=633, y=132, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='文化',
            area=ImagemapArea(
                x=633, y=36, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='外交領事',
            area=ImagemapArea(
                x=833, y=29, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行政',
            area=ImagemapArea(
                x=833, y=130, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='商務',
            area=ImagemapArea(
                x=833, y=230, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='地政/地產',
            area=ImagemapArea(
                x=833, y=330, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行銷',
            area=ImagemapArea(
                x=833, y=430, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='英文',
            area=ImagemapArea(
                x=833, y=530, width=160, height=70
                     )
                )

            ]
        )
    ]   
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))


        
def subject(array):
    data = pd.read_excel('關鍵詞表.xlsx',sheet_name="關鍵詞表(推薦)")
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
    
    text_1="科系 : "
    text_2="跨領域 : "
    text_3="第二專長 : "

    for i in range(len(derpar)):
        if i==0:
            text_1+=derpar[i]
        else:
            text_1 = text_1+" ,"+derpar[i]
            
    if len(cross_f) >= 1:
        for i in range(len(cross_f)):
            if i==0:
                text_2+=cross_f[i]
            else:
                text_2 = text_2+" ,"+cross_f[i]

    else:
        pass
    if len(second_spe) >= 1:
        for i in range(len(second_spe)):
            if i==0:
                text_3+=second_spe[i]
            else:
                text_3 = text_3+" ,"+second_spe[i]

    else:
        pass
    
    text = text_1 +"\n"+ text_2 +"\n"+text_3
    
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
  return rows.get(number)

def arrange_holland(file):
  second_specialty_rows = {}
  cross_domain_rows = {}
  auxiliary_department_rows = {}
  double_major_rows = {}
  with open(file, "r", encoding="big5") as fp:
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

sec_spec_rows,cro_dom_rows,aux_dep_rows,dou_maj_rows = arrange_holland('Holland .csv')

def return_course(holland_code):
  sec_spec = '第二專長：'
  cro_dom = '跨領域學分學程：'
  aux_dep = '輔系：'
  dou_maj = '雙主修：'
  if len(holland_code) == 5:
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    sec_spec = sec_spec[:-2]
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    cro_dom = cro_dom[:-2]
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    aux_dep = aux_dep[:-2]
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    dou_maj = dou_maj[:-2]
    return sec_spec + '\n' + cro_dom + '\n' + aux_dep + '\n' + dou_maj
  elif len(holland_code) == 3:
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if len(value) > 3:
        value = value[:-2]
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    sec_spec = sec_spec[:-2]
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if len(value) > 3:
        value = value[:-2]
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    cro_dom = cro_dom[:-2]
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if len(value) > 3:
        value = value[:-2]
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    aux_dep = aux_dep[:-2]
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if len(value) > 3:
        value = value[:-2]
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    dou_maj = dou_maj[:-2]
    return sec_spec + '\n' + cro_dom + '\n' + aux_dep + '\n' + dou_maj
  elif len(holland_code) == 1:
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")[0]
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    sec_spec = sec_spec[:-2]
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")[0]
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    cro_dom = cro_dom[:-2]
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")[0]
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    aux_dep = aux_dep[:-2]
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")[0]
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    dou_maj = dou_maj[:-2]
    return sec_spec + '\n' + cro_dom + '\n' + aux_dep + '\n' + dou_maj







      
 
  

    
       


