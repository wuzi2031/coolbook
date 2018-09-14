import json

from locust import HttpLocust, TaskSet, task


# locust -f locust_try.py --host=https://www.baidu.com
class UserBehavior(TaskSet):
    def on_start(self):
        self.tokenInfo = None
        self.headers = {"Content-type": "application/json"}
        data = json.dumps({"username": "admin", "password": "wzm123456"})

        with self.client.request(method='post', url='/login/', data=data, headers=self.headers) as response:
            if response.status_code == 200:
                self.tokenInfo = json.loads(response.content)['token']
                print("tokenInfo:", self.tokenInfo)
                self.headers.update({'Authorization': 'Token ' + self.tokenInfo})
                print("LOGIN RESULT:", self.headers)

    @task(1)
    def apk_config(self):
        with self.client.get("/apk_config", headers=self.headers) as response:
            if response.status_code == 200:
                print("apk_config:", response.status_code, response.content)


class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    host = 'http://47.106.145.133'
    min_wait = 3000
    max_wait = 6000
