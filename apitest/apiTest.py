import unittest, logging
from apitest.httpRequests import HttpUtil, Method


class UserOptionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        url = 'https://tm.tita.com/api/v1/106454/113590608/Signin/AddV4'
        header = {'Authorization': 'x_5v173tnORrokFXY68G_1k_4PDgYBKNp94Fp3XErhQwVu49KJ7Wig'}
        body = {
            "device_code": "864031036855112",
            "gcj_coordate": "",
            "wgs_coordate": "",
            "wifi_macaddress": "38:ff:36:78:a2:18"}
        hUtil = HttpUtil()
        re = hUtil.request(url=url,
                           method=Method.POST,
                           header=header,
                           body=body)
        print(re)
        self.assertEqual(re[0]['code'], 401)


if __name__ == '__main__':
    unittest.main(verbosity=2)
