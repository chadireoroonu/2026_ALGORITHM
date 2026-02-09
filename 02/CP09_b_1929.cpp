// 소수 구하기
// https://www.acmicpc.net/problem/1929
// https://chadireoroonu.tistory.com/348

#include <iostream>
#include <vector>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    
    int M, N;
    cin >> M >> N;

    vector<bool> nums(N + 1, true);
    nums[0] = nums[1] = false;

    for (int i = 2; i * i <= N; i++) {
        if (nums[i]) {
            for (int j = i * i; j <= N; j += i) {
                nums[j] = false;
            }
        }
    }

    for (int i = M; i <= N; i++) {
        if (nums[i]) {
            cout << i << '\n';
        }
    }

    return 0;
}