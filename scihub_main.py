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
        
        print('正在查找'+url)
        
        if url.count('scholar.google.com'):
            
            limit = int(input('输入搜索文章数:'))
            
            result = sh.search(url,limit)
            # fetch specific article (don't download to disk)
            # this will return a dictionary in the form 
            # {'pdf': PDF_DATA,
            #  'url': SOURCE_URL,
            #  'name': UNIQUE_GENERATED NAME
            # }       
        else:
            result = sh.fetch(url)
            
        if not 'url' in result:
            print('未找到'+url)
            print(result['err'])
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
                print(resdown['err'])
            
    isexit = input('是否退出?(y/n)')

    