# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# https://chadireoroonu.tistory.com/353

def solution(lottos, win_nums):
    free = lottos.count(0)    
    correct = len(set(lottos) & set(win_nums))
    
    return [min(6, 7 - correct - free), min(6, 7 - correct)]
