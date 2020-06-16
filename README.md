# scihub.py

scihub.py是一个sci-hub.cc的非官方的python接口，可以在实现从谷歌学术搜索论文并从sci-hub.cc下载论文的操作。目前Sci-Hub下载和谷歌学术搜索均可用，如有问题请联系我。

## Sci-Hub网址查询
- 国内使用网址为http://tool.yovisun.com/scihub/ 
- 国外使用网址为https://sci-hub.now.sh/
- 备用网址为https://lovescihub.wordpress.com/

## 安装依赖项
```
pip install -r requirements.txt
```
## 使用Sci-Hub

- 运行`scihub_main.py`
- 按提示输入url或doi(多个以;隔开)
- 如果查找到则自动下载到当前目录

## 使用谷歌学术

- 确保VPN开启全局模式
- 运行`gscholar_main.py`
- 按提示输入关键词和文章数目
- 如果查找到则自动下载到当前目录

## 常见问题

- 打开即闪退：sci-hub网址挂了，自行更换上述网址
- 没有搜索到相关文章
	- 报错connection error：VPN挂了或者无网络，自行更换VPN
	- 报错captcha：网络繁忙，重试一次