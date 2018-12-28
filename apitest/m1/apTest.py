import random
import time

from cmq.tlib.base import BaseCase
from cmq.tlib.request.httpRequests import Http, Method
from cmq.tlib.uri import Mind


class ApiTest(BaseCase):
    DEBUG = True

    def before(self):
        pass

    def after(self):
        self.http.close()

    def random_32(self):
        seed = "1234567890abcdef"
        sa = []
        for i in range(32):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        return salt

    def random_24(self):
        seed = "1234567890"
        sa = []
        for i in range(24):
            sa.append(random.choice(seed))
        salt = ''.join(sa)
        return salt

    # def test_tt(self):
    #     self.assertEqual(False, True)

    def test_login(self):
        i = 1
        while (i > 0):
            time.sleep(2)
            header = {'Content-Type': 'application/json',
                      'kry-api-brand-id': '32316'}
            self.http = Http(header=header, timeout=3)
            tradeUuid = self.random_32()  # 'f13d5f6092a04f61bda70cc547965099'
            uuid = self.random_32()  # '743cd426cdb447dc8fefe3e2c8b84346'
            tradeNo = self.random_24()  # '101180803135946517000809'
            mind = Mind(self)
            u = mind.address()
            url = u + '/CalmRouter/v1/trade/submit'
            body = {
                "appType": "5",
                "brandID": 32316,
                "content": {
                    "brandIdenty": 32316,
                    "businessType": 1,
                    "changed": True,
                    "clientCreateTime": 1533276067659,
                    "clientUpdateTime": 1533276067659,
                    "creatorId": 120682522773404672,
                    "creatorName": "袁娟",
                    "deliveryType": 1,
                    "deviceIdenty": "cc:b8:a8:93:0d:9c",
                    "domainType": 1,
                    "privilegeAmount": 0.0,
                    "saleAmount": 13.0,
                    "shopIdenty": 810094551,
                    "skuKindCount": 1,
                    "source": 10,
                    "sourceChild": 1,
                    "statusFlag": 1,
                    "tradeAmount": 13.0,
                    "tradeAmountBefore": 13.0,
                    "tradeDeposit": {
                        "brandIdenty": 32316,
                        "changed": True,
                        "depositPay": 1,
                        "shopIdenty": 810094551,
                        "statusFlag": 1,
                        "tradeUuid": tradeUuid,
                        "uuid": uuid
                    },
                    "tradeExtra": {
                        "brandIdenty": 32316,
                        "changed": True,
                        "clientCreateTime": 1533276067646,
                        "clientUpdateTime": 1533276067646,
                        "creatorId": 120682522773404672,
                        "creatorName": "袁娟",
                        "deliveryPlatform": 1,
                        "deviceIdenty": "cc:b8:a8:93:0d:9c",
                        "shopIdenty": 810094551,
                        "statusFlag": 1,
                        "tradeUuid": tradeUuid,
                        "updatorId": 120682522773404672,
                        "updatorName": "袁娟",
                        "uuid": uuid
                    },
                    "tradeExtras": [
                        {
                            "brandIdenty": 32316,
                            "changed": True,
                            "clientCreateTime": 1533276067646,
                            "clientUpdateTime": 1533276067646,
                            "creatorId": 120682522773404672,
                            "creatorName": "袁娟",
                            "deliveryPlatform": 1,
                            "deviceIdenty": "cc:b8:a8:93:0d:9c",
                            "shopIdenty": 810094551,
                            "statusFlag": 1,
                            "tradeUuid": tradeUuid,
                            "updatorId": 120682522773404672,
                            "updatorName": "袁娟",
                            "uuid": uuid
                        }
                    ],
                    "tradeItemExtraDinners": [],
                    "tradeItemExtras": [],
                    "tradeItems": [
                        {
                            "actualAmount": 12.0,
                            "amount": 12.0,
                            "brandIdenty": 32316,
                            "changed": True,
                            "clientCreateTime": 1533276067652,
                            "clientUpdateTime": 1533276067652,
                            "creatorId": 120682522773404672,
                            "creatorName": "袁娟",
                            "deviceIdenty": "cc:b8:a8:93:0d:9c",
                            "enableWholePrivilege": 1,
                            "feedsAmount": 0,
                            "guestPrinted": 2,
                            "isChangePrice": 2,
                            "issueStatus": 2,
                            "itemSource": 1,
                            "price": 12.0,
                            "propertyAmount": 0,
                            "quantity": 1,
                            "saleType": 2,
                            "shopIdenty": 810094551,
                            "skuId": 120686618654144512,
                            "skuName": "青椒肉丝",
                            "skuUuid": "e9504cd1ac1a485bb791ce7c175f2001",
                            "sort": 0,
                            "statusFlag": 1,
                            "tradeUuid": tradeUuid,
                            "type": 0,
                            "unitName": "克",
                            "updatorId": 120682522773404672,
                            "updatorName": "袁娟",
                            "uuid": uuid
                        }
                    ],
                    "tradeNo": tradeNo,
                    "tradePayForm": 1,
                    "tradePayStatus": 1,
                    "tradePeopleCount": 1,
                    "tradeStatus": 3,
                    "tradeTime": 1533275986516,
                    "tradeType": 1,
                    "updatorId": 120682522773404672,
                    "updatorName": "袁娟",
                    "uuid": uuid
                },
                "deviceID": "cc:b8:a8:93:0d:9c",
                "nationInfos": [
                    {}
                ],
                "opVersionUUID": "cb1a4dc6ec0b4d9a8fd87959afe898f7",
                "shopID": 810094551,
                "systemType": "android",
                "timeZone": "Etc/GMT+8",
                "versionCode": "2110081500",
                "versionName": "8.15.0"
            }
            try:
                re = self.http.request(url=url,
                                       method=Method.POST,
                                       data=body)
                print(re)
            except Exception as e:
                print(e)
            i = i - 1
            self.http.close()
