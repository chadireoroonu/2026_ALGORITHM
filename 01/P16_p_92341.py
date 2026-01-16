# 주차 요금 계산
# https://school.programmers.co.kr/learn/courses/30/lessons/92341
# https://chadireoroonu.tistory.com/342

from math import ceil

def solution(fees, records):
    answer = []
    parking, total = {}, {}
    
    for r in records: # 입력처리
        time, num, type = list(r.split(' '))
        minutes = int(time[:2]) * 60 + int(time[3:])
        if type == 'IN': # 입차 시간 기록
            parking[num] = minutes
        else: # 입차 시간으로 주차 시간 계산
            intime = parking.pop(num)
            total[num] = total[num] + minutes - intime if num in total else minutes - intime
    
    for num, intime in parking.items(): # 출차 안 한 차들 주차 시간 계산
        total[num] = total[num] + 1439 - intime if num in total else 1439 - intime
    
    for car in sorted(total): # 차량별 주차요금 계산
        if total[car] <= fees[0]: # 기본시간 내
            answer.append(fees[1])
        else: # 기본시간 외
            answer.append(fees[1] + ceil((total[car] - fees[0]) / fees[2]) * fees[3])

    return answer