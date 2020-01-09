"""
@Author: wu_zhiming
@Time: 2019/12/25
@Desc: 
@Copyright:
"""

import re
import sys


class Computer:
    ADD = '+'
    RED = '-'
    MUT = '*'
    DIV = '/'
    LE = '('
    RI = ')'
    CLEAN = 'clean'
    EXIT = 'exit'
    __sum = 0

    def visit_sum(self):
        print('结果:' + str(self.__sum))

    def add(self, a, b):
        return a + b

    def reduce(self, a, b):
        return a - b

    def multi(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            print('被除数不能为0')
            return None
        else:
            return a / b

    def check_input(self, input_info):
        input_info = input_info.replace(' ', '')  # 去除空格
        if Computer.ADD in input_info or Computer.RED in input_info or Computer.MUT in input_info or Computer.DIV in input_info:
            info_mark = ''.join(re.split('\d+', input_info))  # 数子移除后的字符串
            last_str = info_mark.replace(Computer.ADD, '').replace(Computer.RED, '').replace(Computer.MUT, '').replace(
                Computer.DIV, '').replace(Computer.LE, '').replace(Computer.RI, '').replace('.', '')  # 运算符移除后的字符串
            if last_str == '':
                return input_info
            else:
                return None
        else:
            return None

    def gen_express_arr(self, input_info):
        # input_info = '(' + input_info + ')'
        info_arr = []
        last_is_num = False
        data = None
        last_index = len(input_info) - 1
        for index, s in enumerate(input_info):
            if s is Computer.LE or s is Computer.RI:
                if last_is_num == True:
                    info_arr.append(data)
                info_arr.append(s)
                last_is_num = False
            elif s.isdigit() or s is '.':
                if last_is_num == True:
                    data = data + s
                else:
                    data = s
                if (index == last_index):
                    info_arr.append(data)
                last_is_num = True
            elif s is Computer.ADD or s is Computer.RED or s is Computer.MUT or s is Computer.DIV:
                if last_is_num == True:
                    info_arr.append(data)
                info_arr.append(s)
                last_is_num = False
        return info_arr

    def base_compute(self, a, b, op):
        result = None
        if op is Computer.ADD:
            result = self.add(a, b)
        elif op is Computer.RED:
            result = self.reduce(a, b)
        elif op is Computer.MUT:
            result = self.multi(a, b)
        elif op is Computer.DIV:
            result = self.div(a, b)
        return result

    def isdigit(self, str):
        try:
            float(str)
            return True
        except:
            return False

    def compute_arr(self, arr):
        # print('compute_arr---', arr)
        if not self.isdigit(arr[0]):
            arr.insert(0, self.__sum)
        index_values = []
        for index, value in enumerate(arr):
            if value is Computer.MUT or value is Computer.DIV:
                index_values.append(index)
        index_values.sort()
        result_sub = None
        for value in index_values:
            result_sub = self.base_compute(float(arr[value - 1]), float(arr[value + 1]), arr[value])
            arr[value + 1] = str(result_sub)
            arr[value] = None
            arr[value - 1] = None
        arr2 = [a for a in arr if a != None]
        last_index = len(arr2) - 1
        for index, a in enumerate(arr2):
            if not self.isdigit(a) and index is not 0:
                if index is not last_index:
                    result_sub = self.base_compute(float(arr2[index - 1]), float(arr2[index + 1]), arr2[index])
                    arr2[index + 1] = str(result_sub)
                    arr2[index] = None
                    arr2[index - 1] = None
        return result_sub

    def compute_exp(self, exp_arr):
        print(exp_arr)
        exp_count = 0
        sub_exp_dict = {exp_count: []}
        for value in exp_arr:
            max_count = max(sub_exp_dict.keys())
            if value is Computer.LE:
                exp_count = exp_count + 1
                sub_exp_dict.update({exp_count: []})
            elif value is Computer.RI:
                arr_max = sub_exp_dict.get(max_count)
                sub_result = self.compute_arr(arr_max)
                sub_exp_dict.get(exp_count).append(sub_result)
                # sub_exp_dict.update({exp_count: sub_result})
                r_second_count = max_count - 1
                if r_second_count >= 0:
                    arr_secnd = sub_exp_dict.get(r_second_count)
                    arr_secnd.append(str(sub_result))
                    del sub_exp_dict[max_count]
                    exp_count = exp_count - 1
            else:
                arr_max = sub_exp_dict.get(max_count)
                arr_max.append(str(value))
        result = self.compute_arr(sub_exp_dict.get(0))
        self.__sum = result

    def start(self):
        print('请输入:')
        while (True):
            input_info = input()
            # try:
            if (Computer.CLEAN == input_info):
                self.__sum = 0
                self.visit_sum()
            elif (Computer.EXIT == input_info):
                sys.exit(0)
            else:
                input_info = self.check_input(input_info)
                if (input_info):
                    self.compute_exp(self.gen_express_arr(input_info))
                    self.visit_sum()
                else:
                    print('输入的格式不正确')
        # except Exception as e:
        #     # print(e)
        #     print('计算有误，请重试')


Computer().start()
