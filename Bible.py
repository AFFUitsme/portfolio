# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:13:14 2018

@author: AFFU
"""

file=open('bible.txt','r')

vol_key=[]

vol_value=[]

ch_sli=[]

while True:
    content=file.readline()
    sli_vol=[]    
    for i in content:
        if i.isnumeric()==True and i !='一' and i != '二' and i != '三':
            ch_sli_start=content.index(i)
            break
        else:
            sli_vol+=i
    for i in content:
        if i==':':
            ch_sli_end=content.index(i)
    sli_vol2=''.join(sli_vol)
    if sli_vol2 == '':
        break
    elif sli_vol2 not in vol_key:
        vol_key.append(sli_vol2)
        vol_value.append([])         
    else:
         pass
    ch_sli.append(content[ch_sli_start:ch_sli_end])
    
file.close()

file=open('bible.txt','r')

tempchlevel=''

tempvollevel=''

j=-1

for i in range(len(ch_sli)):
    content=file.readline()
    ch_index=ch_sli[i]
    sli_vol=[]    
    for k in content:
        if k==':':
            ver_sli_start=content.index(k)+1
        elif k==' ':
            ver_sli_end=content.index(k)
            break
    for t in content:
        if t.isnumeric()==True and t !='一' and t != '二' and t != '三':
            break
        else:
            sli_vol+=t
    sli_vol2=''.join(sli_vol)
    vol_index=sli_vol2
    if vol_index != tempvollevel:
        tempvollevel=vol_index
        j+=1
        vol_value[j].append([])
        if ch_index != tempchlevel:
            tempchlevel=ch_index
            vol_value[j].append([])
            if int(content[ver_sli_start:ver_sli_end])<10:
                str_li_con=list(content)
                str_li_con.insert(ver_sli_end,' ')
                str_con_2="".join(str_li_con)            
                vol_value[j][int(tempchlevel)-1].append(str_con_2[ver_sli_start:-1])
            else:
                vol_value[j][int(tempchlevel)-1].append(content[ver_sli_start:-1])
        else:
            if int(content[ver_sli_start:ver_sli_end])<10:
                str_li_con=list(content)
                str_li_con.insert(ver_sli_end,' ')
                str_con_2="".join(str_li_con)            
                vol_value[j][int(tempchlevel)-1].append(str_con_2[ver_sli_start:-1])
            else:
                vol_value[j][int(tempchlevel)-1].append(content[ver_sli_start:-1])
    else:
        if ch_index != tempchlevel:
            tempchlevel=ch_index
            vol_value[j].append([])
            if int(content[ver_sli_start:ver_sli_end])<10:
                str_li_con=list(content)
                str_li_con.insert(ver_sli_end,' ')
                str_con_2="".join(str_li_con)            
                vol_value[j][int(tempchlevel)-1].append(str_con_2[ver_sli_start:-1])
            else:
                vol_value[j][int(tempchlevel)-1].append(content[ver_sli_start:-1])
        else:
            if int(content[ver_sli_start:ver_sli_end])<10:
                str_li_con=list(content)
                str_li_con.insert(ver_sli_end,' ')
                str_con_2="".join(str_li_con)            
                vol_value[j][int(tempchlevel)-1].append(str_con_2[ver_sli_start:-1])
            else:
                vol_value[j][int(tempchlevel)-1].append(content[ver_sli_start:-1])
        
bible=dict(zip(vol_key,vol_value))

print(vol_key)

print(bible['約'][1-1][1-1])
                
        
    