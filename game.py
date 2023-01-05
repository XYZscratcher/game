"""
Author          XYZscratcher github.com/xyzscratcher
LastModified    2023/1/5
License         MIT
URL             github.com/xyzscratcher/game

Windows10 系统 + Python3.10 亲测可运行
"""
import os
import hashlib
import json
import time
import winsound
import pdb

# 返回当前程序所在的目录
def get_dirname()->str:
    return os.path.dirname(os.path.abspath(__file__))

重开次数=0
回答次数=0
金币数量=0
salt=b"9e24d797-7114-4596-9e44-0b6193df23cf"# MD5 加密时用到的“盐”
exit=False
try:
    with open(get_dirname()+'\game-data.json', 'r',encoding="utf-8") as f:
        game_data = json.load(f)
    with open(get_dirname()+"\game-data.txt","r") as t:
        x=t.read()
    if x==hashlib.md5(str(game_data).encode()+salt).hexdigest(): # 检查 game-data.json 的 MD5 值与 game-data.txt 的数据是否相同，如果不同，程序停止运行。
        重开次数=game_data["重开次数"]
        金币数量=game_data["金币数量"]
    else:
        print("你修改了游戏数据，游戏自动停止运行！")
        exit=True
except OSError:
    pass
# 游戏中的“台词”
taici_1_1="""
"""
taici_1_2="""
"""
taici_1_3=""""""

# 逐字输出效果
def _say(words:str,sec=0.06,is_start=False):
    i=1
    x="</"
    while i<=len(words):
        print('\r'+words[0:i],end="")
        if words[i-1]!=" ":
            time.sleep(sec)
        i+=1
    if not is_start:
        i=1
        while i<=len(x):
            print('\r'+words+x[0:i],end="")
            time.sleep(sec)
            i+=1
        i=len(x)-1
        while i>=0:
            #pdb.set_trace()
            print('\r'+words+x[0:i]+" "*(len(words)+len(x)),end='')
            time.sleep(sec)
            i-=1
# 游戏主要用到的输出函数，用“]]”分组。用“ENTER”键转到下一个组。
def say(words:str,start=False,bg=False):
    words=words.split("]]\n")
    if not start:
        for i in words:
            x=i.split("\n")
            for j in x:
                _say(j)
                print()# 换行
                time.sleep(0.6)
            print()
    else:
        for i in words:
            x=i.split("\n")
            for j in x:
                if not bg:
                    _say(j.center(190," "),sec=0.01,is_start=True)
                else:
                    _say(j.center(190," "),is_start=True)
                print()# 换行
                time.sleep(0.6)
            if not bg:
                input()
                os.system("cls")
            else:
                print()
            #print('-'*25)
# 制作游戏中的问题。这些问题往往能改变游戏情节的走向。
def 制作问题(op:list)->int:
    global 回答次数
    for i in op:
        print("- "+i)
    if 回答次数==0:
        print("<请输入你选择的选项的序号，如1、2、3>")
    else:
        回答次数+=1
    def 收集回答():
        try:
            你的回答=int(input())
            if 你的回答>len(op) or 你的回答==0:
                raise IOError
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
            return 收集回答()
        except IOError:
            print(f"只有{len(op)}个选项，你回答个{你的回答}是啥意思？")
            return 收集回答()
        else:
            return 你的回答
    return 收集回答()
def die():
    print("上帝使用白魔法复活了你。\n你可以重新开始。")
    input()
    global 重开次数
    重开次数+=1
    game_data={"重开次数":重开次数,"金币数量":金币数量}
    with open(get_dirname()+"\game-data.json","w",encoding="utf-8") as f:
        json.dump(game_data,f,ensure_ascii=True)
    with open(get_dirname()+"\game-data.txt","w") as t:
        """
        为了防止玩家篡改游戏数据，这里将游戏数据用 MD5 加密，保存至 game-data.txt。
        每次打开游戏时，都会检查 game-data.json 的 MD5 值与 game-data.txt 的数据是否相同，如果不同，程序停止运行。
        """
        md5_data=hashlib.md5(str(game_data).encode(encoding="utf-8")+salt)
        md5_data_str=md5_data.hexdigest()
        t.write(md5_data_str)
    main()
def main():
    taici_0=f"""蒲公英计划
{"="*50}
<按 ENTER 键开始>"""
    taici_bg=f"""随着人类技术水平的不断提高，
人类社会的方方面面都有着突飞猛进的进步。]]
但同时，我们的家园——地球也被严重污染：
天空是灰色的，
海洋是灰色的，
河流也是灰色的；
森林早已被人类全部砍伐，
空气也变得有毒……
地球——这位人类的母亲，正被她的子孙无情的伤害。]]
2178 年，科学家预测，地球的生态系统将于二十年内完全崩溃。
于是，联合国抛弃了地球，启动了代号为“蒲公英”的星际移民计划。]]
“蒲公英”计划
"""
    #print(get_root_dirname()+"\game-data.json")
    os.system("color 87")
    winsound.PlaySound(get_dirname()+r"\bgm.wav",winsound.SND_FILENAME|winsound.SND_ASYNC|winsound.SND_LOOP)# 播放背景音乐
    say(taici_bg,start=True,bg=True)
    say(taici_0,True)
    #回答1=制作问题(["","",""])
    """
    if 回答1==1:
        say(taici_1_1)
        die()
    elif 回答1==2:
        say(taici_1_2)
    else:
        say()
    """
if not exit:
    main()
