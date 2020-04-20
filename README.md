HttpScan - 一个龟速HTTP服务发现程序
---
2019年9月份写的，当时是因为一个项目用nmap扫端口的时候没有发现开放9090的http服务端口，项目结束提交出去后，另一家乙方在9090上发现了严重漏洞，导致我们很尴尬，然后我就含着愧疚写下了这个垃圾扫描器。在网盘吃灰好久了，今天翻到就想着发出来，算是一段屈辱史吧。

垃圾程序，大佬莫喷

Usage
---
* python3 HttpScan.py -u http://example.com
* python3 HttpScan.py -u xx.xx.xx.xx

PS：线程默认是1000，-t可指定线程，结果会保存在result.txt里



![Image 1.png](https://i.loli.net/2020/04/20/6DxckrNp2jz49eH.png)