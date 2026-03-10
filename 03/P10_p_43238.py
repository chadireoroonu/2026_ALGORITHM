# 입국심사
# https://school.programmers.co.kr/learn/courses/30/lessons/43238
# https://chadireoroonu.tistory.com/351

def solution(n, times):
    answer = 0
    
    front, rear = 0, times[-1] * n # 최소, 최대 시간 설정
    while front <= rear:
        mid = (front + rear) // 2 # 심사 소요 시간
        total = 0 # 시간 안에 입국심사 가능한 사람 수
        for t in times: # 각 심사대에서 검사할 수 있는 사람 확인
            total += mid // t
            if total >= n: # 이미 모든 사람을 검사했다면 종료
                break
        
        # 현재 시간 안에 모든 사람을 심사할 수 있다면 시간 줄이기
        if total >= n:
            answer = mid
            rear = mid - 1
        else: # 현재 시간 안에 모든 사람을 심사할 수 없다면 시간 늘리기
            front = mid + 1
        
    return answer