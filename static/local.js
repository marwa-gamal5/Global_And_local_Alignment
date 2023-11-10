function myfunction() {
    const form = document.getElementById('form');
    const First_Seq = document.getElementById('First_Seq');
    const Second_Seq = document.getElementById('Second_Seq');
    localStorage.setItem("first-seq", First_Seq.value);
    localStorage.setItem("second-seq", Second_Seq.value);
    const form2 = document.getElementById('form2');
    const Match = document.getElementById('Match');
    const MisMatch = document.getElementById('MisMatch');
    const Gap = document.getElementById('Gap');
    localStorage.setItem("match-s", Match.value);
    localStorage.setItem("mismatch-s", MisMatch.value);
    localStorage.setItem("gap-s", Gap.value);
    window.location.href="local_align.html";
}