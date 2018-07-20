# _*_ coding:utf-8 _*_
__author__ = 'imbaqian'
__date__ = '2018/7/20 15:56'

import requests
import json

class YunPian(object):
    def __init__(self, apikey):
        self.api_key = apikey
        self.single_send_url = "https://sms.yunpian.com/v2/sms/single_send.json"

    def send(self, code, mobile):
        parmas = {
            "apikey": self.api_key,
            "mobile": mobile,
            "text": "【尚前先生】您的验证码是{code}。如非本人操作，请忽略本短信".format(code=code),
        }

        response = requests.post(self.single_send_url, data=parmas)
        re_dict = json.loads(response.text)
        return re_dict

if __name__ == '__main__':
    yunpian = YunPian("apikey")
    yunpian.send("验证码", "手机号")