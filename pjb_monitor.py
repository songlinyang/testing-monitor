import requests
import unittest



class PjbMonitor():

    def __init__(self):
        self.core_status = False
        self.bank_status = False
        self.cash_status = False
        self.user_status = False
        self.message_status = False
        self.other_status = False
        self.activity_status = False
        self.job_status = False

    def core_listen(self):
        core_swagger_url = "http://183.62.139.101:18084/pj-p2p-core/swagger-ui.html"
        while True:
            print("----监听core-----")
            resp = requests.get(core_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False



    def bank_listen(self):
        bank_swagger_url = "http://183.62.139.101:18084/pj-p2p-bank/shanghaiBank2/rabbit"
        while True:
            print("----监听bank-----")
            resp = requests.get(bank_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def cash_listen(self):
        cash_swagger_url = "http://183.62.139.101:18084/pj-p2p-cash/swagger-ui.html"
        while True:
            print("----监听cash-----")
            resp = requests.get(cash_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def user_listen(self):
        user_swagger_url = "http://183.62.139.101:18084/pj-p2p-user/swagger-ui.html"
        while True:
            print("----监听user-----")
            resp = requests.get(user_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def message_listen(self):
        message_swagger_url = "http://183.62.139.101:18084/pj-p2p-message/swagger-ui.html"
        while True:
            print("----监听message-----")
            resp = requests.get(message_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def other_listen(self):
        other_swagger_url = "http://183.62.139.101:18084/pj-p2p-other/swagger-ui.html"
        while True:
            print("----监听other-----")
            resp = requests.get(other_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def activity_listen(self):
        activity_swagger_url = "http://183.62.139.101:18084/pj-p2p-activity/swagger-ui.html"
        while True:
            print("----监听activity-----")
            resp = requests.get(activity_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def job_listen(self):
        job_swagger_url = "http://183.62.139.101:18084/pj-p2p-job/swagger-ui.html"
        while True:
            print("----监听job-----")
            resp = requests.get(job_swagger_url)
            if resp.status_code == 200:
                yield True
                break
            else:
                yield False

    def monitor_start(self):
        # 使用协程，调度各个微服务Swagger接口，监听启动结果

        while True:
            if self.core_status == False:
                self.core_status = self.core_listen().__next__()
            if self.bank_status == False:
                self.bank_status = self.bank_listen().__next__()
            if self.cash_status == False:
                self.cash_status = self.cash_listen().__next__()
            if self.user_status == False:
                self.user_status = self.user_listen().__next__()
            if self.message_status == False:
                self.message_status = self.message_listen().__next__()
            if self.other_status == False:
                self.other_status = self.other_listen().__next__()
            if self.activity_status == False:
                self.activity_status = self.activity_listen().__next__()
            if self.job_status == False:
                self.job_status = self.job_listen().__next__()
            if self.core_status and self.bank_status and self.cash_status and self.user_status and self.message_status and self.other_status and self.activity_status and self.job_status:
                print("core/bank/cash/user/message/other/activity/job服务均已启动完毕！")
                break

    def run(self):
        self.monitor_start()



if __name__ == "__main__":
    monitor = PjbMonitor()
    monitor.run()
