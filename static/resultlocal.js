const firstseq =localStorage.getItem('first-seq');
const secondseq =localStorage.getItem('second-seq');
document.getElementById('first-seq').textContent=firstseq;
document.getElementById('second-seq').textContent=secondseq ;
const matchs =localStorage.getItem('match-s')
const mismatchs =localStorage.getItem('mismatch-s')
const gaps =localStorage.getItem('gap-s')
document.getElementById('match-s').textContent=matchs;
document.getElementById('mismatch-s').textContent=mismatchs ;
document.getElementById('gap-s').textContent= gaps;