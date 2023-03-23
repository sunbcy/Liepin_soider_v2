# https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=3937c8c4-ba15-458b-8f06-eb3db814d668

# -d '{"msgtype":"text","text":{"content":"Hello world"}}'
import json
import requests

class QiyeWeChat_Bot():
    def __init__(self,wechat_url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',key=''):
        self.wechat_url=wechat_url
        self.key=key
        
    def send_text(self,msg,mention_set=()):
        headers={"Content-Type":"application/json"}
        if len(mention_set)>=1:
            mentioned_mobile_list=[mobiles[name] for name in mention_set]
            para={'msgtype':'text',
            'text':{'content':msg,'mentioned_mobile_list':mentioned_mobile_list}}
        else:
            para={'msgtype':'text',
            'text':{'content':msg}}
        # print(wechat_url+key)
        res=requests.post(self.wechat_url+self.key,data=json.dumps(para),headers=headers)
        print("<{status_code}>".format(status_code=res.status_code))
        # quit()
        return res.text
        
if __name__=='__main__':
    Bot_1=QiyeWeChat_Bot(wechat_url,key)
    send_cnt='Hello World,爱你们哦'
    ret=Bot_1.send_text(send_cnt)
    print(ret)