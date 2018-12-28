DATA = {
    'data_bases': {
        'trade': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "testingplatform",
            'USER': 'root',
            'PASSWORD': "Wzm@123456",
            'HOST': "127.0.0.1"
        },
        'not_trade': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "testingplatform",
            'USER': 'root',
            'PASSWORD': "Wzm@123456",
            'HOST': "127.0.0.1"
        },
    },
    'urls': {
        'erp': "http://cierp.com",
        'mind': "https://calm4.dd.com"
    },
    'selenium_drivers': [
        {'host': '', 'port': ''},
        {'host': '', 'port': ''}
    ]
    ,
    'appium_drivers': [
        {
            'dp700': {
                'device_name': 'dp700',
                'app_package': '',
                'app_activity': '',
                'host': '',
                'port': '',
                'platform_version': '',
            }
        },
        {
            'dp700': {
                'device_name': 'dp7001',
                'app_package': '',
                'app_activity': '',
                'host': '',
                'port': '',
                'platform_version': '',
            }
        },
        {
            'huawei_nova': {
                'device_name': 'huawei_nova',
                'app_package': '',
                'app_activity': '',
                'host': '',
                'port': '',
                'platform_version': '',
            }
        }
    ]
}
