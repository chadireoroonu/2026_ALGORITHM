// 자릿수 더하기
// https://school.programmers.co.kr/learn/courses/30/lessons/12931
// https://chadireoroonu.tistory.com/338

int solution(int n)
{
    int answer = 0;
    
    while (n) {
        answer += n % 10;
        n = n / 10;
    }

    return answer;
}