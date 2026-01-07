# 귤 고르기
# https://school.programmers.co.kr/learn/courses/30/lessons/138476
# https://chadireoroonu.tistory.com/336

def solution(k, tangerine):
    sizes = [0] * (max(tangerine) + 1)
    
    for t in tangerine:
        sizes[t] += 1
    
    sizes.sort(reverse=True)
    
    for i in range(len(sizes)):
        if sizes[i] >= k:
            return i + 1
        
        sizes[i + 1] = sizes[i] + sizes[i + 1]
