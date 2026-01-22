// 문자열 내 p와 y의 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/12916
// https://chadireoroonu.tistory.com/345

function solution(s){
    let p = 0, y = 0
    
    for (let c of s) {
        if (c == 'p' | c == 'P') p++
        else if (c == 'y' | c == 'Y') y++
    }

    return p == y ? true : false
}
