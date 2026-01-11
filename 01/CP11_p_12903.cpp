// 가운데 글자 가져오기
// https://school.programmers.co.kr/learn/courses/30/lessons/12903
// https://chadireoroonu.tistory.com/339

#include <string>

using namespace std;

string solution(string s) {
    int n = s.length();

    return (n % 2) ? s.substr(n / 2, 1) : s.substr(n / 2 - 1, 2);
}