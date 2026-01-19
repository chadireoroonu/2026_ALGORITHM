# 다음 큰 숫자
# https://school.programmers.co.kr/learn/courses/30/lessons/12911
# https://chadireoroonu.tistory.com/343

# 아이디어
# 2진수로 변환 -> binary
# 맨 뒤에 있는 1의 인덱스 찾기 -> oneidx
# oneidx 앞에 있는 0 인덱스 찾기 -> zeroidx
# answer = binary[:zeroidx] + '1' + '0' * (len(n) - oneidx)
# answer 총 binary 길이가 될때까지 += 1
# 10진수 변환

def solution(n):
    answer = 0
    binary = '0' + bin(n)[2:]
    
    oneidx = binary.rfind('1')
    zeroidx = binary[:oneidx].rfind('0')
    answer = binary[:zeroidx] + '1' + '0' * (len(binary) - oneidx)
    answer += '1' * (len(binary) - len(answer))

    return int(answer, 2)