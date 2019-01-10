var button = document.getElementById("theme")
var body = document.getElementsByTagName("body")[0]
var item = localStorage.getItem("themeSetting")
var navbar = document.getElementById("navbar")
var econtent = document.getElementById("econtent")
var footer = document.getElementById("footer")
var cards = document.getElementsByClassName("card")

if (item == "dark") {
    button.checked = true
    toggle()
    button.innerHTML = " Dark Mode"
} else {
    button.checked = false
    button.innerHTML = " Light Mode"
}

/*  This is a really annoying thing I had to do to hotfix bootstrap because for some stupid reason, bootstrap refuses to render
    'invalid-feedback' elements without having 'd-block' added to them. Idiocy. This has been a reported bug for a while.
*/
var invalidFeedbackElements = document.getElementsByClassName("invalid-feedback")
for (var i = 0; i < invalidFeedbackElements.length; i++) {
    invalidFeedbackElements[i].classList.add("d-block")
}


function toggle() {
    body.classList.toggle("dark")
    navbar.classList.toggle("navbar-dark")
    navbar.classList.toggle("bg-dark")
    econtent.classList.toggle("text-light")
    footer.classList.toggle("dark")
    button.classList.toggle("btn-dark")
    for (var i = 0; i < cards.length; i++) {
        cards[i].classList.toggle("bg-dark")
    }
}

function toggleTheme() {
    if (localStorage.getItem("themeSetting") == "light") {
        localStorage.setItem("themeSetting", "dark")
        button.innerHTML = " Dark Mode"
    } else {
        localStorage.setItem("themeSetting", "light")
        button.innerHTML = " Light Mode"
    }
    toggle()
}

function deleteBrokenImage(image) {
    var img = document.getElementById(image)
    img.parentNode.removeChild(img)
}