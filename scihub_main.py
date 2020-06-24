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
    for num in range(len(url_list)):
        print(url_list[num])
    
    for ind,url in enumerate(url_list):

        print('正在查找第{}篇...'.format(ind+1))
        # fetch specific article (don't download to disk)
        # this will return a dictionary in the form 
        # {'pdf': PDF_DATA,
        #  'url': SOURCE_URL,
        #  'name': UNIQUE_GENERATED NAME
        # } 
        result = sh.fetch(url)
            
        if 'err' in result:
            print('错误：' + result['err'])
        else:
            print('已找到第{}篇...'.format(ind+1))    
            # exactly the same thing as fetch except downloads the articles to disk
            # if no path given, a unique name will be used as the file name
            print('正在下载第{}篇...'.format(ind+1))
            resdown = sh.download(result['url'])
            if 'err' in resdown:
                print('错误：' + resdown['err'])
            else:
                print('下载成功！')
                
            
    isexit = input('是否退出?(y/n)')

    