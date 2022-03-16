from django.conf import settings

from linebot import LineBotApi

from linebot.models import TextSendMessage


from linebot.models import TemplateSendMessage, MessageTemplateAction, ButtonsTemplate,ConfirmTemplate, PostbackTemplateAction,PostbackAction
from linebot.models import ImagemapSendMessage, BaseSize, ImagemapAction, ImagemapArea, MessageImagemapAction
from iteration_utilities import duplicates
from iteration_utilities import unique_everseen
import os
import pandas as pd
import csv
import numpy as np


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def begin(event):  #多項傳送
    try:
        message = [  #串列
            TextSendMessage(  
            text = "叮咚叮！答對了\n歡迎進入森林～"
            ), 
            TextSendMessage(  
            text = "小圖作為森林的嚮導，將竭盡所能地向你推薦雙修輔系灌木、跨域學程洞穴和第二專長小溪中，可能符合你胃口的跨域蘿蔔坑！"
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
        
def 先不用(event): 
    try:
        message = TextSendMessage(text='(T▽T) 有甚麼問題想問我嗎～還是你目前不想要尋找蘿蔔坑呢？歡迎你留言給小圖哦！') 
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤！'))
        
        

def 提供關鍵詞(event):  
    try:
        message = [  #串列
            TextSendMessage(  
            text = "٩(●ᴗ●)۶ 好的，那麼我們開始啦～"
             ), 
            TextSendMessage(  
            text = "首先，請你從下方兩個籃子中點選三個符合你口味的跨領域紅蘿蔔，讓我為你推薦蘿蔔坑喔～"
             ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/qDsM6xm.png",
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
            text='歷史',
            area=ImagemapArea(
                x=53, y=154, width=160, height=70
              )
            ),
        MessageImagemapAction(
             text='哲學',
            area=ImagemapArea(
                x=49, y=258, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='政治',
            area=ImagemapArea(
                x=52, y=360, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社會',
            area=ImagemapArea(
                x=51, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='社工',
            area=ImagemapArea(
                x=43, y=555, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='英文',
            area=ImagemapArea(
                x=248, y=350, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='物理',
            area=ImagemapArea(
                x=249, y=547, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='數學',
            area=ImagemapArea(
                x=247, y=449, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='德文',
            area=ImagemapArea(
                x=246, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='日文',
            area=ImagemapArea(
                x=246, y=154, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='音樂',
            area=ImagemapArea(
                x=248, y=54, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='微生物',
            area=ImagemapArea(
                x=441, y=149, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='心理',
            area=ImagemapArea(
                x=440, y=252, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='法律',
            area=ImagemapArea(
                x=439, y=352, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='經濟',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='會計',
            area=ImagemapArea(
                x=438, y=541, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='企管',
            area=ImagemapArea(
                x=628, y=59, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='經營',
            area=ImagemapArea(
                x=832, y=47, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='管理',
            area=ImagemapArea(
                x=639, y=540, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='資科',
            area=ImagemapArea(
                x=641, y=459, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='資管',
            area=ImagemapArea(
                x=635, y=351, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='財精',
            area=ImagemapArea(
                x=634, y=251, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='國貿',
            area=ImagemapArea(
                x=635, y=148, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='創意/創作',
            area=ImagemapArea(
                x=831, y=152, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='人文',
            area=ImagemapArea(
                x=834, y=258, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='非營利組織',
            area=ImagemapArea(
                x=833, y=357, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='東亞',
            area=ImagemapArea(
                x=837, y=453, width=160, height=70
                )
            ),
         MessageImagemapAction(
            text='全英語',
            area=ImagemapArea(
                x=840, y=546, width=160, height=70
                )
            ),
         MessageImagemapAction(
             text='化學',
            area=ImagemapArea(
                x=442, y=48, width=160, height=70
            )
           )
         ],
        ),
            ImagemapSendMessage(
            base_url= "https://imgur.com/cgOUHGo.png",
            alt_text='關鍵詞表2',
      base_size=BaseSize(width=1040, height=650),
      actions=[
        MessageImagemapAction(
            text='財經',
            area=ImagemapArea(
                x=43, y=51, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='科技',
            area=ImagemapArea(
                x=45, y=164, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='中國',
            area=ImagemapArea(
                x=48, y=261, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='幸福',
            area=ImagemapArea(
                x=48, y=361, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='在地',
            area=ImagemapArea(
                x=47, y=453, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='創新',
            area=ImagemapArea(
                x=49, y=555, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='永續',
            area=ImagemapArea(
                x=245, y=559, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='影視',
            area=ImagemapArea(
                x=239, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='台灣',
            area=ImagemapArea(
                x=235, y=353, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='人權',
            area=ImagemapArea(
                x=244, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='經典',
            area=ImagemapArea(
                x=244, y=159, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='美學',
            area=ImagemapArea(
                x=246, y=52, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='推理',
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
            text='分析',
            area=ImagemapArea(
                x=439, y=348, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='公共治理',
            area=ImagemapArea(
                x=445, y=449, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='韓文',
            area=ImagemapArea(
                x=435, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='高齡',
            area=ImagemapArea(
                x=635, y=545, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行為',
            area=ImagemapArea(
                x=633, y=459, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='健康生活',
            area=ImagemapArea(
                x=635, y=345, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='線性代數',
            area=ImagemapArea(
                x=630, y=252, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='翻譯',
            area=ImagemapArea(
                x=633, y=151, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='文化',
            area=ImagemapArea(
                x=626, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='外交領事',
            area=ImagemapArea(
                x=833, y=54, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行政',
            area=ImagemapArea(
                x=839, y=153, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='商務',
            area=ImagemapArea(
                x=833, y=256, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='地政/地產',
            area=ImagemapArea(
                x=830, y=356, width=160, height=70
                )
            ),
        MessageImagemapAction(
            text='行銷',
            area=ImagemapArea(
                x=834, y=451, width=160, height=70
                )
            ),
        MessageImagemapAction(
             text='理財',
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
    
    text_1="雙輔系灌木叢："
    text_2="跨域學程洞穴："
    text_3="第二專長小溪："

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
  if len(rows.get(number)) > 5:
    return rows.get(number)[:5]
  elif len(rows.get(number)) <= 5:
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
  sec_spec = '第二專長小溪：'
  cro_dom = '跨域學程洞穴：'
  aux_dep = '輔系：'
  dou_maj = '雙輔系灌木叢：'
  
  if len(holland_code) > 5:
    holland_code = holland_code[:5]
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    if sec_spec ==sec_spec:
        pass
    else:
        sec_spec = sec_spec[:-2]
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    if cro_dom ==cro_dom:
        pass
    else:
        cro_dom = cro_dom[:-2]
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    if aux_dep ==aux_dep:
        pass
    else:
        aux_dep = aux_dep[:-2]
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    if dou_maj ==dou_maj:
        pass
    else:
       dou_maj = dou_maj[:-2]
    return dou_maj + '\n' + cro_dom  + '\n' + sec_spec
  
  if len(holland_code) == 5:
    for key, value in sec_spec_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        sec_spec = sec_spec + key + ', '
    if sec_spec ==sec_spec:
        pass
    else:
        sec_spec = sec_spec[:-2]
    for key, value in cro_dom_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        cro_dom = cro_dom + key + ', '
    if cro_dom ==cro_dom:
        pass
    else:
        cro_dom = cro_dom[:-2]
    for key, value in aux_dep_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        aux_dep = aux_dep + key + ', '
    if aux_dep ==aux_dep:
        pass
    else:
        aux_dep = aux_dep[:-2]
    for key, value in dou_maj_rows.items():
      value = value.replace(" ","")
      if value == holland_code:
        dou_maj = dou_maj + key + ', '
    if dou_maj ==dou_maj:
        pass
    else:
       dou_maj = dou_maj[:-2]
    return dou_maj + '\n' + cro_dom  + '\n' + sec_spec

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
    return dou_maj + '\n' + cro_dom  + '\n' + sec_spec

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
    return dou_maj + '\n' + cro_dom  + '\n' + sec_spec

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
    elif '跨域學程洞穴' in item:
      for i in item[7:].split(','):
        cro_dom.append(i)
  for item in pre_holand_ans:
    if '雙輔系灌木叢' in item:
      for i in item[7:].split(','):
        aux_dep.append(i)
    elif '第二專長小溪' in item:
      for i in item[7:].split(','):
        sec_spec.append(i)
    elif '跨域學程洞穴' in item:
      for i in item[7:].split(','):
        cro_dom.append(i)

  aux_dep = [i for i in aux_dep if i != '']
  sec_spec = [i for i in sec_spec if i != '']
  cro_dom = [i for i in cro_dom if i != '']
 
  aux = '雙輔系灌木叢：'
  sec = '第二專長小溪：'
  cro = '跨域學程洞穴：'
  if list(unique_everseen(duplicates(aux_dep))) != []:
    aux += list(unique_everseen(duplicates(aux_dep)))[0]
  if list(unique_everseen(duplicates(sec_spec))) != []:
    sec += list(unique_everseen(duplicates(sec_spec)))[0]
  if list(unique_everseen(duplicates(cro_dom))) != []:
    cro += list(unique_everseen(duplicates(cro_dom)))[0]

  return aux + '\n' + sec + '\n' + cro
