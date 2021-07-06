function display_Kr() {
    var eng = document.getElementsByClassName('en')
    var kor = document.getElementsByClassName('kr')

    for (var en = 0; en < eng.length; en++) {
        eng[en].style.display = 'none'
    }
    for (var kr = 0; kr < kor.length; kr++) {
        kor[kr].style.display = 'inline'
    }
    //window.scrollTo(0,0)
}
function display_En() {
    var eng = document.getElementsByClassName('en')
    var kor = document.getElementsByClassName('kr')

    for (var en = 0; en < eng.length; en++) {
        eng[en].style.display = 'inline'
    }
    for (var kr = 0; kr < kor.length; kr++) {
        kor[kr].style.display = 'none'
    }
    //window.scrollTo(0,0)
}
