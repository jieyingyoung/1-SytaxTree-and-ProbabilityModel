import random

human_language = '''
human = 自己 寻找 活动
自己 = 我 | 俺 | 我们
寻找 = 看看 | 找找 | 想找点儿
活动 = 乐子 | 玩儿的
'''

reception_language = '''
host = 寒暄 报数 询问 业务相关 结尾
寒暄 = 称谓 打招呼 | 打招呼
称谓 = 人称 ，
人称 = 先生 | 女士 | 小朋友
打招呼 = 您好 | 你好 
报数 = 我是 数字 号 ，
数字 = 单个数字 | 数字 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
询问 = 请问你要 | 您需要
业务相关 = 玩玩 具体业务
玩玩 = 耍一耍 | 玩一玩
具体业务 = 打牌 | 喝酒 | 打猎 | 赌博
结尾 = 吗？
'''

poem = '''
yongE = 拟声词 ， 承 转 合
拟声词 = 鹅鹅鹅 | 嘎嘎嘎 | 汪汪汪 | 咩咩咩
承 = adj body pre place 押韵动词 ,
转 = color body verb color place ,
adj =  直 | 美 | 大 | 小 | 丑 | 胖 | 瘦
body =  脖 | 脸 | 腿 | 爪 | 掌 | 角
pre = 向 | 朝 | 往 | 奔 
place = 天 | 地 | 水 | 湖 | 海 | 草 | 石 | 树
color = 白 | 绿 | 红 | 蓝 | 黑 | 清 | 紫 | 橙 | 黄
verb = 打 | 拍 | 挑 | 碰 | 撩  
押韵动词 = 歌 | 泼 | 挪 | 乐 | 咳 | 活 | 拨 
合 = color body verb color 押韵地点 .
押韵地点 = 波 | 窝 | 座 | 车 | 泊
'''

psychologist = '''
psychologist = 寒暄 选座位 我是 姓名 ， 工号 数字 ， 职位 询问 结尾 ？
寒暄 = 时间 好 , 
时间 = 早上 | 中午 | 下午 | 晚上 | 夜里
选座位 = 选一个 人称 喜欢的座位吧！ 
人称 = 你 | 您 
姓名 = 张三 | 李四 | 王二麻子 | 狗蛋  
数字 = 数字 单个数字 | 单个数字
单个数字 = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 
职位 = 国家 级别 心理咨询师 ，
级别 = 二级 | 三级
询问 = 请问 哪个 能够 帮助 人称 
能够 = 能 | 可以
哪个 = 有什么 | 有哪些
结尾 = 的吗 | 的呢 
'''

def generate(gramma_rule, target): # gramma_rule is a dictionary, target is the key
    if target in gramma_rule: # because target may not in the gramma_rule
        candidates = gramma_rule[target]  # take the contents of the dictionary gramma_rule , which key is 'target'
        # candidates = [c.strip() for c in candidates] # to remove the whitespace
        candidate = random.choice(candidates) #randomly take one of the candidates
        again = [generate(gramma_rule,target = c.strip()) for c in candidate.split()] # for the case of 'name names', then repeat itself
        return ''.join(again) # to remove the whitespace in candidate
    else:
        return target

def get_generation_by_gram(gramma_str, target, equal_split = '=', or_split = '|'):
    rules = dict()

    for line in gramma_str.split('\n'):
        if not line: continue # skip the empty lines
        key, contents = line.split(equal_split)
        content = contents.split(or_split)
        #print(key,'\n',content)
        rules[key.strip()] = content
        # strip(): returns a new string after removing any leading and trailing whitespaces including tabs (\t).
        # rstrip(): returns a new string with trailing whitespace removed. It’s easier to remember as removing white spaces from “right” side of the string.
        # lstrip(): returns a new string with leading whitespace removed, or removing whitespaces from the “left” side of the string.

    generated = generate(rules,target = target)
    return generated

def generate_n(rules,target,number_sentence):
    generated_sentences = [get_generation_by_gram(rules,target) for i in range(number_sentence)]
    return generated_sentences

print(get_generation_by_gram(human_language, target = 'human'))
print(get_generation_by_gram(reception_language, target = 'host'))
# print(get_generation_by_gram(poem, target = 'yongE'))
# print(get_generation_by_gram(psychologist, target = 'psychologist'))

# generate_n(poem, 'yongE', 4)
print(generate_n(psychologist,'psychologist', 3))

