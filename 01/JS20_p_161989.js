// 덧칠하기
// https://school.programmers.co.kr/learn/courses/30/lessons/161989
// https://chadireoroonu.tistory.com/344

function solution(n, m, section) {
    return section.reduce((acc, s) => {
        if (s > acc.last) {
            acc.answer++
            acc.last = s + m - 1
        }
        return acc;
    }, { answer: 0, last: 0 }).answer
}
