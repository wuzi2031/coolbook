import unittest, logging
from apitest import httpRequests


class UserOptionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        header = {'Authorization': 'x_5v173tnORrokFXY68G_1k_4PDgYBKNp94Fp3XErhQwVu49KJ7Wig'}
        body = {
            "device_code": "864031036855112",
            "gcj_coordate": "",
            "wgs_coordate": "",
            "wifi_macaddress": "38:ff:36:78:a2:18"}
        hUtil = httpRequests.HttpUtil(url='https://tm.tita.com/api/v1/106454/113590608/Signin/AddV4',
                                      method=httpRequests.Method.POST,
                                      header=header,
                                      body=body)
        re = hUtil.request()
        print(re)


if __name__ == '__main__':
    unittest.main(verbosity=2)
