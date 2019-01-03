#coding=utf-8

import dataProvider
import checkCondition

path = r'F:\PycharmProjects\data_check'
file = 'bcgame.csv'

max_value = 10000
step = 1

sample_num = 1000
minimum_sample_num = 1000

cut_num = 10

check_number = 100
max_diff = 5

if __name__ == '__main__':
    data = dataProvider.load_csv_data(path, file)
    result1 =  checkCondition.check_condition1(data, max_value, step)
    result2 = checkCondition.check_condition2(data, max_value, sample_num, minimum_sample_num)
    result3 = checkCondition.check_condition3(data, cut_num)
    check_mean, check_max = checkCondition.check_condition4(data, check_number, max_diff)