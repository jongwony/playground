# -*- coding: utf-8 -*-
# python 2.x
import re
from urllib2 import urlopen

# html 코드 내용 저장
web = urlopen("http://www.example.com")
html = web.read()
web.close()

# 윈도우 형식 변경 
# code = str(html).encode('utf-8').decode('cp949')

# <title></title>
# 대소문자 구별, 개행문자도 .으로 구별
c = re.compile(r'.*?<title.*?>(.*)</title>', re.I|re.S)

# 탭에 적혀있는 문구(title) 출력
print c.findall(str(html))

