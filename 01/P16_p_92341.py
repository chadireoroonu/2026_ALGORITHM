# 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# https://chadireoroonu.tistory.com/342

from math import ceil

def solution(fees, records):
    answer = []
    parking, total = {}, {}
    
    def calculate(n, t): # 차량별 주차 시간 더하기
        total[n] = total[n] + t - parking[n] if n in total else t - parking[n]
        return
    
    for r in records: # 입력처리
        time, num, type = list(r.split(' '))
        if type == 'IN': # 입차차량 기록
            parking[num] = int(time[:2]) * 60 + int(time[3:])
        else: # 출차차량 주차 시간 계산
            calculate(num, int(time[:2]) * 60 + int(time[3:]))
            parking.pop(num) # 입차 목록에서 삭제
    
    for p in parking: # 출차 안 한 차들 주차 시간 계산
        calculate(p, 23 * 60 + 59)
    
    cars = sorted(total) # 차량 번호 순 정렬용
    
    for c in cars: # 차량별 주차요금 계산
        if total[c] <= fees[0]: # 기본시간 내
            answer.append(fees[1])
        else: # 기본시간 외
            over = ceil((total[c] - fees[0]) / fees[2])
            answer.append(fees[1] + over * fees[3])

    return answer