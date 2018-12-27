def compare_two_dict(compared_dict, contain_dict):
    """
    判断是否包含另一个dict，有数组的情况暂不支持
    :param compared_dict:
    :param contain_dict: 被包含的dict
    :return:
    """
    flag = True
    if (compared_dict and contain_dict):
        if (isinstance(compared_dict, dict) and isinstance(contain_dict, dict)):
            contain_keys = contain_dict.keys()
            compared_keys = compared_dict.keys()
            if ([True for k in contain_keys if k in compared_keys]):
                for key in contain_keys:
                    if (flag == False):
                        break
                    c_value = contain_dict.get(key)
                    cd_value = compared_dict.get(key)
                    if (isinstance(c_value, dict) and isinstance(cd_value, dict)):
                        flag = compare_two_dict(cd_value, c_value)
                    elif (isinstance(c_value, list) and isinstance(cd_value, list)):
                        for cc_value in c_value:
                            pass
                    else:
                        if (c_value != cd_value):
                            flag = False
        else:
            raise ('参数类型不为dict')
    return flag


if __name__ == '__main__':
    dict1 = {
        'a': {
            'e': 5
        },
        'b': 2,
        'c': 3,
        'd': {
            'e': 5
        }
    }
    dict2 = {
        'a': {
            'e': 5
        },

        'c': 3,
        'd': {
            'e': 5
        }
    }

    key_list = ['a', 'c', 'b', 'e']
    result = compare_two_dict(dict1, dict2)
    print(result)
    print(dict1==dict2)