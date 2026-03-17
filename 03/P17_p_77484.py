# 로또의 최고 순위와 최저 순위
# https://school.programmers.co.kr/learn/courses/30/lessons/77484
# https://chadireoroonu.tistory.com/353

def solution(lottos, win_nums):
    answer = [7, 7]
    free = lottos.count(0)
    lottos = set(lottos) - {0}
    win_nums = set(win_nums)
    
    correct = len(lottos & win_nums)
    answer[0] -= correct + free if correct + free else 1
    answer[1] -= correct if correct else 1
    
    return answer
