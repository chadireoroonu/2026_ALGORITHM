# 지폐 접기
# https://school.programmers.co.kr/learn/courses/30/lessons/340199

def solution(wallet, bill):
    answer = 0
    
    wmini, wmaxi = sorted(wallet)
    bmini, bmaxi = sorted(bill)
    
    while True:
        if wmini >= bmini and wmaxi >= bmaxi:
            break
            
        else:
            answer += 1
            bmaxi //= 2
            
            if bmini > bmaxi:
                bmini, bmaxi = bmaxi, bmini
    
    return answer