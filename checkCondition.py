#coding=utf-8

import numpy as np
import pandas as pd

def check_condition1(data, max_value, step):
    '''
    condition1: Find the minimun value of explosion point where the condition P(X>A) > 1/A happens for the first time.
                The bigger rtn is, the better data will be.

    :param data: array,   data to be checked
    :param max_value: int,  assumed max value of explosion point
    :param step: float,  step between each explosion point
    :return: float,   minimun value of explosion point where the condition P(X>A) > 1/A happens for the first time
    '''
    data_num = len(data)
    num = (max_value - 1) / step + 1
    sample_series = np.linspace(1, max_value, num)
    prob_list = []
    prob_stantard_list = []
    for i in range(int(num)):
        this_flag = data > sample_series[i]
        this_index = np.where(this_flag)[0]
        prob_list.append(len(this_index) / data_num)
        prob_stantard_list.append(1 / sample_series[i])
    diff_arr = np.array(prob_list) - np.array(prob_stantard_list)
    diff_flag = diff_arr > 0
    diff_index = np.where(diff_flag)[0]
    return diff_index[0] + 1


def check_condition2(data, max_value, sample_num, minimum_sample_num):
    '''
    condition2: check the independence of the X
                the smaller rtn is, the better data will be.
    :param data: array,   data to be checked
    :param max_value: int,   assumed max value of explosion point
    :param sample_num: int,   how manny explosion points will be sampled randomly
    :param minimum_sample_num: int,  the minimun of data length
    :return: float
    '''
    data_num = len(data)
    if 2 * minimum_sample_num >= data_num:
        print('please prepare enough data, more than {0}!'.format(2 * minimum_sample_num))
        return 1
    else:
        random_series = np.random.rand(sample_num)
        sample_series = random_series * (max_value - 1) + 1
        std_list = []
        for i in range(sample_num):
            this_flag = data > sample_series[i]
            this_index = np.where(this_flag)[0]
            this_index_num = len(this_index)
            this_prob_series = []
            for j in range(this_index_num):
                if this_index[j] < data_num - minimum_sample_num:
                    this_prob_series.append((this_index_num-j) / (data_num - this_index[j]))
            std_list.append(np.std(this_prob_series))
    return np.mean(std_list)


def check_condition3(data, cut_num):
    '''
    condition3: when continuously cut, check the similarity of each part of data
                the smaller rtn is, the better data will be
    :param data: array,  data to be checked
    :param cut_num: int,  how many part will be cut into
    :return: float
    '''
    data_num = len(data)
    if data_num / cut_num < 10:
        print('please prepare enough data!')
        return 1
    else:
        cut_index = np.ceil(np.linspace(0, data_num, cut_num + 1))
        mean_list = []
        var_list = []
        kurtosis_list = []
        skewness_list = []
        for i in range(cut_num):
            this_data = data[cut_index[i]:cut_index[i+1]]
            this_data_df = pd.DataFrame(this_data)
            mean_list.append(this_data_df.mean())
            var_list.append(this_data_df.var())
            kurtosis_list.append(this_data_df.kurt())
            skewness_list.append(this_data_df.skew())
        mean_std = np.std(mean_list)
        var_std = np.std(np.power(var_list, 1/2))
        kurtosis_std = np.std(np.power(kurtosis_list, 1/3))
        skewness_std = np.std(np.power(skewness_list, 1/4))
        return (mean_std + var_std + kurtosis_std + skewness_std) / 4


def check_condition4(data, number, max_diff):
    '''
    condition4: calc how many time the data is continuiusly bigger than a chosen number

    :param data: data to be checked
    :param number: number chosen
    :param max_diff: max interval to judge the continuity
    :return:
    '''
    this_flag = data > number
    this_index = np.where(this_flag)[0]
    this_diff = np.diff(this_index)
    this_diff_num = len(this_diff)
    count_list_tmp = []
    count_list = []
    count = 1
    for i in range(this_diff_num):
        if this_diff[i] <= max_diff:
            count += 1
        else:
            count = 1
        count_list_tmp.append(count)
    for i in range(this_diff_num):
        if i < this_diff_num:
            if count_list_tmp[i] != 1 and count_list_tmp[i+1] == 1:
                count_list.append(count_list_tmp[i])
        else:
            if count_list_tmp[i] != 1:
                count_list.append(count_list_tmp[i])
    return  np.mean(count_list), np.max(count_list)










