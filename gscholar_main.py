
import sys

# relative path
sys.path.append('.\\scihub')


print('正在启动谷歌学术搜索工具...')
print('请确保VPN已打开全局模式...')

from scihub import SciHub

sh = SciHub()

isexit='n'

while isexit=='n':

    keyword = input('输入关键词:')
    
    limit = int(input('输入搜索文章数:'))
    
    print('正在搜索相关文章...')
    # retrieve 5 articles on Google Scholars related to 'bittorrent'
    results = sh.search(keyword, limit)
    
    if not results['papers']:
        print('没有搜索到相关文章...')
        print(results['err'])
    else:    
        for num in range(len(results['papers'])):
            print(results['papers'][num]['name'])
            
        isdown = input('是否下载?(y/n)')
        
        if isdown=='y':
            
            # download the papers; will use sci-hub.io if it must
            for paper in results['papers']:
                paper_name = paper['name']
                print('正在下载'+paper_name)
                resdown = sh.download(paper['url'])
                if not 'err' in resdown:
                    print('{}下载成功!'.format(paper_name))
                else:
                    print('{}下载失败...'.format(paper_name))
                    print(resdown['err'])
       
    isexit = input('是否退出?(y/n)')