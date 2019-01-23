# -*- coding: utf-8 -*-
import random
menu_list=['蒸羊羔','蒸熊掌','蒸鹿尾儿','烧花鸭','烧雏鸡儿','烧子鹅','卤煮咸鸭','酱鸡','腊肉','松花','小肚儿','晾肉','香肠','什锦苏盘','熏鸡','白肚儿','清蒸八宝猪','江米酿鸭子','罐儿野鸡','罐儿鹌鹑','卤什锦','卤子鹅','卤虾','烩虾','炝虾仁儿','山鸡','兔脯','菜蟒','银鱼','清蒸哈什蚂','烩鸭腰儿','烩鸭条儿','清拌鸭丝儿','黄心管儿','焖白鳝','焖黄鳝','豆鼓鲇鱼','锅烧鲇鱼','烀皮甲鱼','锅烧鲤鱼','抓炒鲤鱼','软炸里脊','软炸鸡','什锦套肠','麻酥油卷儿','熘鲜蘑','熘鱼脯儿','熘鱼片儿','熘鱼肚儿','醋熘肉片儿','熘白蘑','烩三鲜','炒银鱼','烩鳗鱼','清蒸火腿','炒白虾','炝青蛤','炒面鱼','炝芦笋','芙蓉燕菜','炒肝尖儿','南炒肝关儿','油爆肚仁儿','汤爆肚领儿','炒金丝','烩银丝','糖熘饹炸儿','糖熘荸荠','蜜丝山药','拔丝鲜桃','熘南贝','炒南贝','烩鸭丝','烩散丹']
dinner_list=[]

def machine_choice():
    m_choice=random.choice(menu_list)
    answer=input('选择【{0}】吧？Y/N'.format(m_choice))
    if answer.lower()=='y':
        dinner_list.append(m_choice)
        return dinner_list
    elif answer.lower()=='n':
        print('请重新选择',end=',')
        return machine_choice()
    else:
        print('输入错误请重新选择',end=',')
        return machine_choice()

l=machine_choice()
print(l)