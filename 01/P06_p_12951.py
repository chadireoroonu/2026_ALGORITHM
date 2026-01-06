# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# https://chadireoroonu.tistory.com/335

def solution(s):
    answer = [] # 리스트로 수정
    s = ' ' + s
        
    for i in range(1, len(s)):
        # 저장할 글자 문제 요구사항에 맞춰 변환
        char = s[i].lower() if s[i - 1] != ' ' else s[i].upper()
        answer.append(char)
        
    return ''.join(answer)