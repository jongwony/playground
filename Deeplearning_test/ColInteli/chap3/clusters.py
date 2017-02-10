# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
from math import sqrt
import random

def readfile(filename):
    lines = [line for line in file(filename)]

    # 첫 번째 가로줄은 세로줄 제목임
    colnames = lines[0].strip().split('\t')[1:]
    rownames=[]
    data=[]
    for line in lines[1:]:
        p = line.strip().split('\t')
        # 각 가로줄의 첫 번째 세로줄은 가로줄 이름임
        rownames.append(p[0])
        # 가로줄의 나머지 부분이 데이터
        data.append([float(x) for x in p[1:]])
    return rownames, colnames, data

def pearson(v1, v2):
    # 단순 합 계산
    sumx = sum(v1)
    sumy = sum(v2)

    sumxy = sum([v1[i]*v2[i] for i in range(len(v1))])

    # 제곱의 합 계산
    sumx2 = sum([pow(v, 2) for v in v1])
    sumy2 = sum([pow(v, 2) for v in v2])

    # pearson 
    covn = sumxy - sumx*sumy/len(v1)
    rndevx = sumx2 - pow(sumx, 2)/len(v1)
    rndevy = sumy2 - pow(sumy, 2)/len(v1)
    sdn = rndevx * rndevy

    if sdn == 0: return 0
    
    return covn/sdn


def pearson0to2(v1, v2):
    return 1 - pearson(v1, v2)

def hcluster(rows, distance=pearson0to2):
    distances={}
    currentclustid=-1

    # 초기 군집들을 각 가로줄에서 생성
    clust = [bicluster(rows[i], id=i) for i in range(len(rows))]

    while len(clust)>1:
        lowestpair = (0,1)
        closest = distance(clust[0].vec, clust[1].vec)

        # 가장 작은 거리 값을 가지는 쌍
        for i in range(len(clust)):
            for j in range(i+1, len(clust)):
                # distance는 거리 계산 캐시
                if (clust[i].id, clust[j].id) not in distances:
                    distances[(clust[i].id, clust[j].id)]=distance(clust[i].vec, clust[j].vec)

                d = distances[(clust[i].id, clust[j].id)]

                if d < closest:
                    closest = d
                    lowestpair = (i, j)

        # 두 군집 간 평균
        mergevec = [(clust[lowestpair[0]].vec[i]+clust[lowestpair[1]].vec[i])/2.0 for i in range(len(clust[0].vec))]

        # 새로운 군집 생성
        newcluster = bicluster(mergevec, left = clust[lowestpair[0]],
                right = clust[lowestpair[1]],
                distance = closest,
                id = currentclustid)
        
        # 원래 집합 안에 포함되지 않은 군집 id들은 음수
        currentclustid-=1
        del clust[lowestpair[1]]
        del clust[lowestpair[0]]
        clust.append(newcluster)

    return clust[0]

def printclust(clust, labels=None, n=0):
    # 계층 구조를 만들기 위해 들여 씀
    for i in range(n):
        print ' ',
    if clust.id<0:
        # 음수 id값은 트리의 브랜치
        print '-'
    else:
        # 양수 id값은 트리의 종점
        if labels==None: print clust.id
        else: print labels[clust.id]

    # 우측과 좌측 브랜치 출력
    if clust.left!=None: printclust(clust.left, labels=labels, n=n+1)
    if clust.right!=None: printclust(clust.right, labels=labels, n=n+1)

def getheight(clust):
    # 종점인 경우 높이는 1
    if clust.left == None and clust.right == None: return 1

    # 그렇지 않으면 높이는 각 브랜치 높이들의 합
    return getheight(clust.left)+getheight(clust.right)

def getdepth(clust):
    # 종점 거리는 0
    if clust.left == None and clust.right == None: return 0

    # 브랜치의 거리는 양쪽 중 큰 것에 자신의 거리를 더한 값
    return max(getdepth(clust.left), getdepth(clust.right))+clust.distance

def drawdendrogram(clust, labels, jpeg='clusters.jpg'):
    # 높이와 폭
    h = getheight(clust)*20
    w = 1200
    depth = getdepth(clust)

    # 고정 폭에 맞게 비율 조정
    scaling = float(w - 150) / depth

    # 흰색 배경의 새로운 이미지 생성
    img = Image.new('RGB', (w, h), (255,255,255))
    draw=ImageDraw.Draw(img)
    draw.line((0, h/2, 10, h/2), fill=(255,0,0))

    # 첫 번째 노드 그림
    drawnode(draw, clust, 10, (h/2), scaling, labels)
    img.save(jpeg, 'JPEG')

def drawnode(draw, clust, x, y, scaling, labels):
    if clust.id<0:
        h1 = getheight(clust.left)*20
        h2 = getheight(clust.right)*20
        top = y-(h1+h2)/2
        bottom = y+(h1+h2)/2
        # 선 길이
        ll = clust.distance*scaling
        # 이 군집에서 자식들까지 수직선
        draw.line((x, top+h1/2, x, bottom-h2/2), fill = (255,0,0))
        # 왼쪽 항목까지 수평선
        draw.line((x, top+h1/2, x+11, top+h1/2),fill=(255,0,0))
        # 오른쪽 항목까지 수평선
        draw.line((x, bottom-h2/2, x+11, bottom-h2/2), fill=(255, 0, 0))

        # 이 함수로 왼쪽, 오른쪽 노드를 그림
        drawnode(draw, clust.left, x+11, top+h1/2, scaling, labels)
        drawnode(draw, clust.right, x+11, bottom-h2/2, scaling, labels)
    else:
        # 종점이면 항목 라벨을 그림
        draw.text((x+5, y-7), labels[clust.id], (0,0,0))

def transpose(data):
    newdata=[]
    for i in range(len(data[0])):
        newrow = [data[j][i] for j in range(len(data))]
        newdata.append(newrow)
    return newdata

def kcluster(rows, distance=pearson0to2, k=4):
    # 각 점의 최대, 최소값을 구함
    ranges = [(min([row[i] for row in rows]), max([row[i] for row in rows]))
            for i in range(len(rows[0]))]

    # 임의로 선정한 k개의 중심점을 생성
    clusters = [[random.random()*(ranges[i][1]-ranges[i][0])+ranges[i][0]
        for i in range(len(rows[0]))] for j in range(k)]

    lastmatches = None

    for t in range(100):
        print 'Iteration %d' % t
        bestmatches=[[] for i in range(k)]

        # 각 가로줄별로 가장 근접한 중심점을 찾는다
        for j in range(len(rows)):
            row = rows[j]
            bestmatch = 0
            for i in range(k):
                d = distance(clusters[i], row)
                if d < distance(clusters[bestmatch], row):
                    bestmatch = i
            bestmatches[bestmatch].append(j)

        # 이전과 같은 결과이면 완료
        if bestmatches == lastmatches:
            break

        lastmatches = bestmatch

        # 중심점을 멤버들의 평균으로 이동
        for i in range(k):
            avgs = [0.0]*len(rows[0])
            if len(bestmatches[i]) > 0:
                for rowid in bestmatches[i]:
                    for m in range(len(rows[rowid])):
                        avgs[m]+=rows[rowid][m]
                for j in range(len(avgs)):
                    avgs[j] /= len(bestmatches[i])
                clusters[i] = avgs
    
    return bestmatches


class bicluster:
    def __init__(self, vec, left=None, right=None, distance=0.0, id=None):
        self.left = left
        self.right = right
        self.vec = vec
        self.id = id
        self.distance = distance


