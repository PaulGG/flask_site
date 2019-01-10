var button = document.getElementById("theme")
var body = document.getElementsByTagName("body")[0]
var item = localStorage.getItem("themeSetting")
var navbar = document.getElementById("navbar")
var econtent = document.getElementById("econtent")
var footer = document.getElementById("footer")
var theme_text = document.getElementById("themeText")

if (item == "dark") {
    button.checked = true
    toggle()
    theme_text.textContent = " Dark Mode"
} else {
    button.checked = false
    theme_text.textContent = " Light Mode"
}

function toggle() {
    body.classList.toggle("dark")
    navbar.classList.toggle("navbar-dark")
    navbar.classList.toggle("bg-dark")
    econtent.classList.toggle("text-light")
    footer.classList.toggle("dark")
}

function toggleTheme() {
    if (button.checked) {
        localStorage.setItem("themeSetting", "dark")
        theme_text.textContent = " Dark Mode"
    } else {
        localStorage.setItem("themeSetting", "light")
        theme_text.textContent = " Light Mode"
    }
    toggle()
}
