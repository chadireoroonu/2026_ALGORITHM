// 가운데 글자 가져오기
// https://school.programmers.co.kr/learn/courses/30/lessons/12903
// https://chadireoroonu.tistory.com/339

#include <string>

using namespace std;

string solution(string s) {
    string answer = "";
    
    if (s.length() % 2) {
        answer = s[s.length() / 2];
    } else {
        answer = s.substr(s.length() / 2 - 1, 2);
    }
    
    return answer;
}