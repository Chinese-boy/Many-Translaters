import urllib.request
import urllib.parse
import json
a = 5
while a > 0:
        txt = input('输入要翻译的内容:')
        if txt == '0':
                break
                
        else:
                url = 'http://fy.iciba.com/ajax.php?a=fy'
                
                data = {
                'f':'auto',
                't':'auto',
                'w':txt
                }

                data = urllib.parse.urlencode(data).encode('utf - 8')
                wy = urllib.request.urlopen(url,data)
                html = wy.read().decode('utf - 8')
                ta = json.loads(html)
                print(ta['content']['out'])
                a = a - 1
                
