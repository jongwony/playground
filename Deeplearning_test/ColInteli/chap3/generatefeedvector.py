# -*- encoding: utf-8 -*-
import feedparser
import re

# 한 RSS 피드 안에 있는 제목과 단어 출현 횟수 딕셔너리를 리턴
def getwordcounts(url):
    # 피드를 파싱함
    d = feedparser.parse(url)
    wc={}

    # 모든 게시글별로 루프를 돌기
    for e in d.entries:
        if 'summary' in e:
            summary = e.summary
        else:
            summary = e.description

        # 단어 목록을 추출
        words = getwords(e.title+' '+summary)
        for word in words:
            wc.setdefault(word, 0)
            wc[word]+=1
    
    return d.feed.title,wc

def getwords(html):
    # 모든 HTML 태그를 제거
    txt = re.compile(r'<[^>]+>').sub('', html)
    # 비-알파벳 문자들로 단어를 분리
    words=re.compile(r'[^A-Z^a-z]+').split(txt)
    # 소문자로 변환
    return [word.lower() for word in words if word!='']

apcount={}
wordcounts={}
feedlist=[]

for feedurl in file('feedlist.txt'):
    feedlist.append(feedurl)
    title,wc=getwordcounts(feedurl)
    wordcounts[title]=wc
    for word,count in wc.items():
        apcount.setdefault(word,0)
        if count>1:
            apcount[word]+=1

wordlist=[]

for w,bc in apcount.items():
    frac = float(bc)/len(feedlist)
    if frac>0.1 and frac<0.5:
        wordlist.append(w)

out = file('blogdata.txt','w')
out.write('Blog')

for word in wordlist:
    out.write('\t%s' % word)

out.write('\n')

for blog,wc in wordcounts.items():
    out.write(blog)
    for word in wordlist:
        if word in wc:
            out.write('\t%d' % wc[word])
        else: out.write('\t0')
    
    out.write('\n')
