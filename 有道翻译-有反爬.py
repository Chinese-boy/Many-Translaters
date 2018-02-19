import urllib.request
import urllib.parse
import time
import hashlib #提供了常见的摘要算法
import json
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&sessionFrom=null'  #上一次群里面那个失效了 把_o去掉就可以了
u = 'fanyideskweb'
d = input('请输入翻译的内容：')
f = str(int(time.time()*1000))
c = "rY0D^0'nM0}g5Mm1z%1G4"
g = hashlib.md5()
g.update((u + d + f + c).encode('utf-8'))
head = {}
head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:54.0) Gecko/20100101 Firefox/54.0'
head['Host'] = 'fanyi.youdao.com'
head['Referer'] = 'http://fanyi.youdao.com/'
data = {}
data['i'] = d  # 这是我们要翻译的字符串
data['from'] = 'AUTO'
data['to'] = 'AUTO'
data['smartresult'] = 'dict'
data['client'] = u
data['salt'] = f   # 加密用到的盐。这个是我们破解有道反爬虫机制的关键点
data['sign'] = g.hexdigest() # 签名字符串。也是破解反爬虫机制的关键点
data['doctype'] = 'json'
data['version'] = '2.1'
data['keyfrom'] = 'fanyi.web'
data['action'] = 'FY_BY_CL1CKBUTTON'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

req = urllib.request.Request(url, data, head)
response = urllib.request.urlopen(req)
html = response.read().decode('utf-8')
target = json.loads(html)
print('翻译结果： %s ' % (target['translateResult'][0][0]['tgt']))
