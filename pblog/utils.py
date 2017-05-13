# coding: utf-8

import os, sys
import shutil, datetime, markdown

def endwith(*endstring):
    """筛选特定后缀名
    a = endWith('.jpeg', '.jpg', '.png')  # 只识别后缀名为 .jpeg .jpg .png
    files = ['22.jpeg', '111.exe']
    f_file = filter(a, files)  # 文件名列表
    :param endstring:
    :return:
    """
    ends = endstring
    def run(s):
        f = map(s.endswith, ends)
        if True in f: return s
    return run


def generate_template(path, txt):
    """
    md 渲染成 html
    :param path:
    :param txt:
    :return:
    """
    html = markdown.markdown(txt)
    with open(path, 'w+') as f:
        f.write(html)