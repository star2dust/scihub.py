# scihub.py

scihub.py是一个sci-hub.cc的非官方的python接口，可以在实现从谷歌学术搜索论文并从sci-hub.cc下载论文的操作。
目前sci-hub下载可用。谷歌学术搜索仍然报错，挂梯子也不行，待解决。

## 安装依赖项
```
pip install -r requirements.txt
```
## 使用

- 运行`scihub_main.py`
- 按提示输入url或doi(多个以;隔开)
- 如果查找到则自动下载到当前目录
