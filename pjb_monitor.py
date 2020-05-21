import sys
import requests
from DingDing.DingDingrobot import DingDingRobot



class PjbMonitor():

    def __init__(self):
        self.core_status = False


    def core_listen(self):
        core_swagger_url = "https://www.baidu.com"
        while True:
            print("----监听服务-----")
            resp = requests.get(core_swagger_url)
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


            if self.core_status:
                print("服务已启动完毕！")
                robot = DingDingRobot()
                robot.set_job_name(sys.argv[1])
                robot.set_url(sys.argv[2])
                robot.set_at_phone(sys.argv[3])
                robot.talk()
                break

    def run(self):
        self.monitor_start()



if __name__ == "__main__":
    monitor = PjbMonitor()
    monitor.run()
