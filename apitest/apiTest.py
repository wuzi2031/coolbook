import unittest, logging
from apitest import httpRequests


class UserOptionTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_login(self):
        header = {'dd': 'dd'}
        hUtil = httpRequests.HttpUtil(url='https://www.baidu.com',
                                      method=httpRequests.Method.POST,
                                      header=header)
        re = hUtil.request()
        print(re)


if __name__ == '__main__':
    unittest.main(verbosity=2)
