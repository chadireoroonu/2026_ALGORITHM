// 덧칠하기
// https://school.programmers.co.kr/learn/courses/30/lessons/161989
// https://chadireoroonu.tistory.com/344

#include <vector>

using namespace std;

int solution(int n, int m, vector<int> section) {
    int answer = 0;
    int last = 0;
    
    for (int s : section) {
        if (s > last) {
            answer++;
            last = s + m - 1;
        }
    }
    return answer;
}
