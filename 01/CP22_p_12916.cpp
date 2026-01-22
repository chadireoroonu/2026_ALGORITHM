// 문자열 내 p와 y의 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/12916
// https://chadireoroonu.tistory.com/345

#include <string>
using namespace std;

bool solution(string s)
{
    int p = 0, y = 0;
    
    for (char c : s) {
        if (c == 'p' || c == 'P') p++;
        if (c == 'y' || c == 'Y') y++;
    }
    
    return p == y ? 1 : 0;
}
