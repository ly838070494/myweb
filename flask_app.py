#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 创建flask项目目录结构
import os

# 项目名称
app_name = 'flask_app'
# 模板目录
template_dir = 'template'
# 静态文件
static_dir = 'static'
# 启动文件
start_file = 'run.py'
# 模块列表
module_list = ['user', 'goods']
# __init__.py
init_file = '__init__.py'
# view.py
view_file = 'view.py'


def make_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)


def make_file(file):
    if not os.path.exists(file):
        f = open(file, 'w')
        f.close()


def main():
    app_path = os.path.join(app_name, 'app')
    make_dir(app_path)
    template_path = os.path.join(app_path, template_dir)
    make_dir(template_path)
    static_path = os.path.join(app_path, static_dir)
    make_dir(static_path)
    start_file_path = os.path.join(app_path, start_file)
    make_file(start_file_path)

    for mod in module_list:
        module_path = os.path.join(app_path, mod)
        make_dir(module_path)
        init_file_path = os.path.join(module_path, init_file)
        make_file(init_file_path)
        view_file_path = os.path.join(module_path, view_file)
        make_file(view_file_path)
    print('目录创建完毕！')


if __name__ == '__main__':
    main()
