# -*- coding: utf-8 -*-

from math import sqrt

# person1과 person2의 거리 기반 유사도 점수
def sim_distance(prefs, person1, person2):
    # 공통 항목 목록 추출
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1

    # 공통 평가 항목이 없으면 0
    if len(si)==0: return 0

    # 거리 계산
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item], 2)
        for item in prefs[person1] if item in prefs[person2]])

    return sqrt(sum_of_squares)

# 피어슨 상관계수(두 집단의 선형회귀)
def sim_pearson(prefs, p1, p2):
    # 같이 평가한 항목들의 목록
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]:
            si[item]=1

    # 요소들의 갯수
    n = len(si)

    # 공통요소가 없으면 0
    if n==0: return 0

    # 선호도 합산
    sum1 = sum([prefs[p1][item] for item in si])
    sum2 = sum([prefs[p2][item] for item in si])

    # 제곱의 합 계산
    pow1 = sum([pow(prefs[p1][item], 2) for item in si])
    pow2 = sum([pow(prefs[p2][item], 2) for item in si])

    # 곱의 합
    psum = sum([prefs[p1][item]*prefs[p2][item] for item in si])

    # 피어슨 점수 계산
    num = psum - sum1*sum2/n
    den = sqrt((pow1-pow(sum1, 2)/n)*(pow2-pow(sum2, 2)/n))

    if den==0: return 0

    return (num/den)

# 최적의 상대를 구함
def topMatches(prefs, person, n=5, similarity=sim_pearson):
    scores=[(similarity(prefs, person, other), other)
            for other in prefs if other!=person]

    # 최고점 Top 5
    scores.sort()
    scores.reverse()
    return scores[0:n]

def getRecommend(prefs, person, similarity=sim_pearson):
    totals={}
    simSums={}
   
    for other in prefs:
        # 본인을 비교하지 말것
        if other==person: continue

        sim = similarity(prefs, person, other)

        # 0 이하 점수는 무시
        if sim<=0: continue
    
        for item in prefs[other]:
            # 내가 못본 영화 대상
            if item not in prefs[person] or prefs[person][item]==0:
                #유사도 * 점수
                totals.setdefault(item, 0)
                totals[item]+=prefs[other][item]*sim

                #유사도 합계
                simSums.setdefault(item, 0)
                simSums[item]+=sim

    # 정규화된 목록 생성
    rankings = [(total/simSums[item],item) for item,total in totals.items()]

    # 정렬된 목록 리턴
    rankings.sort()
    rankings.reverse()
    return rankings

def transformPrefs(prefs):
    result={}

    for person in prefs:
        for item in prefs[person]:
            result.setdefault(item, {})

            # 물건과 사람을 바꿈
            result[item][person]=prefs[person][item]
    
    return result

def calulateSimilarItems(prefs, n=10):
    # 유사한 항목들을 가진 항목 딕셔너리 생성
    result={}

    # 선호도 -> 항목중심
    itemPrefs=transformPrefs(prefs)
    c=0
    for item in itemPrefs:
        # 큰 데이터 셋을 위해 진척 상태를 갱신
        c+=1
        if c%100==0: print "%d / %d" % (c, len(itemPrefs))

        # 각 항목과 가장 유사한 항목 구하기
        scores = topMatches(itemPrefs, item, n=n, similarity=sim_pearson)
        result[item]=scores
    return result


