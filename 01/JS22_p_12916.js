// 문자열 내 p와 y의 개수
// https://school.programmers.co.kr/learn/courses/30/lessons/12916
// https://chadireoroonu.tistory.com/345

function solution(s){
    const p = (s.match(/p/gi) || []).length
    const y = (s.match(/y/gi) || []).length
    
    return p === y
}
