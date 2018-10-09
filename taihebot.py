import json,urllib,urllib3
from urllib.parse import urlencode
from qqbot import QQBotSlot as qqbotslot, RunBot

def talk(content,userid):
    cs=urllib3.PoolManager()
    url = 'http://www.tuling123.com/openapi/api'
    da = {"key":"df66a6f6cb7b4e6a87ca6bd55a68ccd0","info":content,"userid":userid}
    j = cs.request('GET',url,fields=da)
    j=json.loads(j.data)
    code = j['code']
    if code == 100000:
        recontent = j['text']
    elif code == 200000:
        recontent = j['text']+j['url']
    elif code == 302000 or code ==308000:
        recontent = j['text']+j['list'][0]['info']+j['list'][0]['detailurl']
    elif code == 40004:
        recontent = '泰合小秘书每天只能回答5000个问题，今天已经很累了，泰合小秘书要去休息了哦～～'
    elif code == 40002:
        recontent = '您有什么想对泰合小秘书说的吗？～'
    elif code == 40007:
        recontent = '您输入的数据格式异常，请重新输入！'
    else:
        recontent = '小秘书还没学会怎么回答这句话'
    return recontent


@qqbotslot
def onQQMessage(bot, contact, member, content):
    if '小V' in str(member) or '小v' in str(member) or 'uin2931776030' in str(contact) or 'QQ小冰' in str(member) or '泰合小秘书' in str(member):  # 防止机器人打架
         return
    elif getattr(member, 'uin', None) == bot.conf.qq:  # 防止自嗨
        return
    elif content == '-stop':
        bot.SendTo(contact, '我轻轻的走了，正如我轻轻的来。挥一挥衣袖，忘掉我的所有～～')
        bot.Stop()
    else:
        print(str(contact))
        bot.SendTo(contact,talk(content,member))


RunBot()    # 启动qqbot，如果是插件模式请注释掉此行
