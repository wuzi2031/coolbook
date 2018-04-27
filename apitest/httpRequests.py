import requests
from enum import Enum

class Method(Enum):
    POST='post'
    GET='get'
    DELETE='delete'
    PUT='put'

class HttpUtil:
    def __init__(self,url="", data="", header="", method=Method.GET):
        self.url=url
        self.data=data
        self.__initHeader(header)
        self.method=method

    def __initHeader(self,header):
        self.headers = {'Host': self.url[8:],
                   'Connection': 'keep-alive',
                   'Cache-Control': 'max-age=0',
                   'Accept': 'text/html, */*; q=0.01',
                   'Accept-Encoding': 'gzip,deflate,br',
                   'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6'
                   }
        self.headers.update(header)
        print("header:"+self.headers.__str__())

    def request(self):
        re = object
        isexcept = False
        if self.method == Method.POST:
            try:
                re = requests.post(self.url, headers=self.headers, data=self.data)
                print("re:"+re.__str__())
                re= re.json()
            except Exception as e:
                re = e
                isexcept = True

        if self.method == Method.GET:
            try:
                re = requests.get(self.url, headers=self.header, data=self.data).json()
            except Exception as e:
                re = e
                isexcept = True

        if self.method == Method.DELETE:
            try:
                re = requests.delete(self.url + "/" + self.data).json()
            except Exception as e:
                re = e
                isexcept = True

        if self.method == Method.PUT:
            try:
                re = requests.put(self.url).json()
            except Exception as e:
                re = e
                isexcept = True

        return re, isexcept