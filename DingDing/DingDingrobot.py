# -*- coding:utf-8 -*-
import requests
import json

"""
定义一个钉钉Robot类
"""
class DingDingRobot():

    def __init__(self):
        self.webhook = 'https://oapi.dingtalk.com/robot/send?access_token=cdf0b2717cfb723f863f5acf6ee65c2d5e7d341e55f65745f7bed6341f64b4bf'
        self.__job_name=""
        self.__url=""
        self.__report_name=""
        self.__domain=""
        self.__picture_name=""
        self.__at_all = False
        self.__at_phone=""


    def set_job_name(self,job):
        self.__job_name = job

    def get_job_name(self):
        return self.__job_name

    def set_url(self,url):
        self.__url = url

    def get_url(self):
        return self.__url

    def set_domain(self,domain):
        self.__domain = domain

    def get_domain(self):
        return self.__domain

    def set_report_name(self,new_name):
        self.__report_name = new_name

    def get_report_name(self):
        return self.__report_name

    def set_picture_name(self,new_name):
        self.__picture_name = new_name

    def get_picture_name(self):
        return self.__picture_name

    def set_at_all(self,status):
        self.__at_all = status

    def get_at_all(self):
        return self.__at_all

    def set_at_phone(self,phone):
        self.__at_phone=phone

    def get_at_phone(self):
        return self.__at_phone

    def talk(self):
        at_phone = []
        if self.get_at_phone():
            print(self.get_at_phone())
            at_phone.append(self.get_at_phone())

        print(at_phone)

        headers = {"Content-Type":"application/json"}
        data = {
            "msgtype": "markdown",
            "markdown": {
                "title": "%s服务已启动成功" % (self.get_job_name()),
                "text": "@%s<br/> %s服务已启动成功%s" % (self.get_at_phone(),self.get_job_name(),self.get_url())
            },
            "at": {
                "atMobiles":["13715384224"],
                "isAtAll":False
            }
        }
        requests.post(self.webhook,headers=headers,json=data)
