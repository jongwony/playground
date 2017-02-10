# -*- coding: utf-8 -*-

import urllib2



class crawler:
    # 데이터베이스 이름으로 크롤러 초기화
    def __init__(self, dbname):
        pass

    def __del__(self):
        pass

    def dbcommit(self):
        pass

    # 항목 번호를 얻고 등재되지 않았다면 추가하는 보조 함수
    def getentryid(self, table, field, value, createnew=True):
        return None

    # 개별 페이지를 색인
    def addtoindex(self, url, soup):
        print 'Indexing %s' % url

    # HTML 페이지에서 텍스트 추출(태그 추출은 안함)
    def gettextonly(self, soup):
        return None

    # 공백문자가 아닌 문자들로 단어들을 분리
    def separatewords(self, text):
        return None

    # 이미 색인한 주소라면 true
    def isindexed(self, url):
        return False

    # 두 페이지 간의 링크를 추가
    def addlinkref(self, urlFrom, urlTo, linkText):
        pass

    # 페이지 목록으로 시작해서 넓이 우선검색을 주어진 깊이만큼 수행
    def crawl(self, pages, depth = 2):
        pass

    # 데이터베이스 테이블을 생성
    def createindextables(self):
        pass


