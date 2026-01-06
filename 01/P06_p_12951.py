# JadenCase 문자열 만들기
# https://school.programmers.co.kr/learn/courses/30/lessons/12951
# https://chadireoroonu.tistory.com/335

def solution(s):
    answer = ''
    s = ' ' + s
        
    for i in range(1, len(s)):
        if s[i] == ' ': # 현재 글자가 공백이라면 그대로 공백 추가
            answer += ' '
            continue
        # 현재 글자가 공백이 아니면 내 앞 글자가 공백일 시 대문자 아니면 소문자
        answer += s[i].lower() if s[i - 1] != ' ' else s[i].upper()
        
    return answer
