import requests
from enum import Enum


class Method(Enum):
    POST = 'post'
    GET = 'get'
    DELETE = 'delete'
    PUT = 'put'


class HttpUtil:

    def __initHeader(self, header):
        self.headers = {
                        'Content-Type': 'application/json'
                        }
        self.headers.update(header)



    def request(self, url="", body="", header="", method=Method.GET):
        self.url = url
        self.data = body
        self.__initHeader(header)
        self.method = method
        re = object
        isexcept = False
        if self.method == Method.POST:
            try:
                re = requests.post(self.url, headers=self.headers, data=self.data).json()
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
