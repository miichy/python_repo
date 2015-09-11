#!/usr/bin/env python

# -*- coding=utf-8 -*-



"""

yaml 文件定义需要配置文件和字段

"""



import os

import yaml

import sys



# 针对每个配置文件，根据yaml中解析出来的keys进行替换

def replace_dict_data(dir_path,dict_data,obj_file):

    os.rename(os.path.join(dir_path,obj_file),os.path.join(dir_path,obj_file+".bak"))

    os.chdir(dir_path)

    output_file = open(obj_file+".bak")

    new_file = open(obj_file,'w+')

    new_file.seek(0,0)

    new_file.truncate()

    while 1:

        line = output_file.readline()

        if not line:

            break

        else:

            for k,v in dict_data.iteritems():

                flag = False

                if k in line:

                    new_file.write(k+"="+v+"\n")

                    flag = True

                    break

            if not flag:

                new_file.write(line)



# 获取需要替换的所有配置文件

def get_conf_files(dict_data):

    files_list = dict_data["configurationsequence"]

    return files_list   ## only for test



# 获取section中的某一个配置文件的所有keys

def get_keys_values(dict_data,file_name):

    return dict_data[file_name][0]  ##  dict



def parser():

    cur_abs_path = os.path.abspath(os.path.dirname(sys.argv[0]))

    conf_res = (sys.argv[1])

    des_directory = (sys.argv[2])

    dir_path = os.path.join(os.path.split(os.path.abspath(sys.argv[0]))[0],des_directory)



    config_file = "%s/%s" % (cur_abs_path,conf_res)

    stream = file(config_file,'r')

    data = yaml.load(stream)

    print("=============")

    confs_list = get_conf_files(data)

    for file_name in confs_list:

        #get_keys_values(data,file_name)

        print dir_path,"~~~~~~~~~~~~"

        replace_dict_data(dir_path,get_keys_values(data,file_name),file_name)

    print("=============")





if __name__ == "__main__":

    parser()