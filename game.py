"""
@Author  XYZscratcher github.com/xyzscratcher
@LastModified    2022/12/30
@License MIT
@URL     github.com/xyzscratcher/game
"""
重开次数=0
回答次数=0
# 游戏中的“台词”
taici_1="""【xx的越狱计划】
作者：XYZscratcher
游戏时长：大约 10 分钟
<按 ENTER 键继续>}}}
你是一只倒霉的鸡。
因为好奇心，你闯进了魔法森林，被霸道的魔王虎关进了地下的秘密监狱。}}}
魔王虎不仅霸道，而且食量无敌，一天要吃10只动物。
地下监狱就是它的食物仓库。
你很清楚，在监狱里，必死无疑。
你必须越狱。}}}
你下定决心，在监狱中坚持练功。
终于，在一个月黑风高夜，你找到了机会。}}}
你要做什么？
"""
taici_1_1=""""""
#hua=""
# 游戏主要用到的输出函数，用“}}}”分组。用“ENTER”键转到下一个组。
def say(words):
    words=words.split("}}}")
    i=0
    #global hua
    while i<len(words):
        #hua+=
        input(words[i])
        #hua+="\n"
        i+=1
# 制作游戏中的问题。这些问题往往能改变游戏情节的走向。
def 制作问题(op):
    global 回答次数
    for i in op:
        print("- "+i)
    if 回答次数==0:
        print("<请输入你选择的选项的序号，如1、2、3>")
    else:
        回答次数+=1
    def 收集回答():
        你的回答=input()
        try:
            你的回答=int(你的回答)
            if 你的回答>len(op) or 你的回答==0:
                raise IOError
        except ValueError:
            print("您输入的不是数字，请再次尝试输入！")
            收集回答()
        except IOError:
            print(f"只有{len(op)}个选项，你回答个{你的回答}是啥意思？")
            收集回答()
        else:
            return 你的回答
    return 收集回答()
say(taici_1)
回答1=制作问题(["在墙壁上挖个洞","在地板下挖个洞","用缩骨术钻出监狱"])
if 回答1==1:
    say()
elif 回答1==2:
    pass
else:
    pass
#say(hua)