# 通知到个人企业微信
import json
import requests
from requests.exceptions import SSLError
import traceback
import urllib3
from conf import QYWeChatBotKey

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class QiyeWeChatBot:
    def __init__(self,
                 wechat_url='https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=',
                 key=QYWeChatBotKey):
        self.wechat_url = wechat_url
        self.key = key
        self.mobiles = {
            "name": "phoneNum"
        }

    def send_text(self, msg, mention_set=()):
        proxies = {
            'http': 'http://localhost:7890',
            'https': 'http://localhost:7890'
        }
        headers = {"Content-Type": "application/json"}
        if len(mention_set) >= 1:
            mentioned_mobile_list = [self.mobiles[name] for name in mention_set]
            para = {
                'msgtype': 'text',
                'text': {
                    'content': msg,
                    'mentioned_mobile_list': mentioned_mobile_list
                }
            }
        else:
            para = {
                'msgtype': 'text',
                'text': {
                    'content': msg
                }
            }
        try:
            res = requests.post(self.wechat_url + self.key, data=json.dumps(para), headers=headers)
            print("<{status_code}>".format(status_code=res.status_code))
            return res.text
        except SSLError:
            res = requests.post(self.wechat_url + self.key, data=json.dumps(para), headers=headers, proxies=proxies)
            print("<{status_code}>".format(status_code=res.status_code))
            return res.text
        except Exception:
            traceback.print_exc()


if __name__ == '__main__':
    wxbot = QiyeWeChatBot()
    wxbot.send_text("test")
