# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 10:47:19 2020

@author: Woody
"""

import sys

# relative path
sys.path.append('.\\scihub')

from scihub import SciHub

sh = SciHub()

# url or doi
# url = '10.1109/ASCC.2017.8287158;10.1007/BF00126069;https://hal.archives-ouvertes.fr/hal-02433405'

isexit='n'

while isexit=='n':

    strin = input('输入url或doi(多个以;隔开):')
    
    url_list = strin.split(';')
    
    print('已输入以下url或doi:')
    print(url_list)
    
    for ind,url in enumerate(url_list):
        # fetch specific article (don't download to disk)
        # this will return a dictionary in the form 
        # {'pdf': PDF_DATA,
        #  'url': SOURCE_URL,
        #  'name': UNIQUE_GENERATED NAME
        # }
        print('正在查找'+url)
        result = sh.fetch(url)
        if not 'url' in result:
            print('未找到'+url)
        else:
            print('已找到'+url)    
        # exactly the same thing as fetch except downloads the articles to disk
        # if no path given, a unique name will be used as the file name
        print('正在下载'+url)
        resdown = sh.download(result['url'])
        if not 'err' in resdown:
            print('下载成功！')
        else:
            print('下载失败...')
            
    isexit = input('是否退出?(y/n)')

    