var button = document.getElementById("theme")
var body = document.getElementsByTagName("body")[0]
var item = localStorage.getItem("themeSetting")
var navbar = document.getElementById("navbar")
var econtent = document.getElementById("econtent")
var footer = document.getElementById("footer")
var theme_text = document.getElementById("themeText")

if (item != null) {
    if (item == "dark") {
        button.checked = true
        setDark()
    } else {
        button.checked = false
        setLight()
    }
}

function setDark() {
    if (!body.classList.contains("dark")) {
        body.classList.add("dark")
    }
    if (!navbar.classList.contains("navbar-dark")) {
        navbar.classList.add("navbar-dark")
    }
    if (!navbar.classList.contains("bg-dark")) {
        navbar.classList.add("bg-dark")
    } 
    if (!econtent.classList.contains("text-light")) {
        econtent.classList.add("text-light")
    }
    if (!footer.classList.contains("dark")) {
        footer.classList.add("dark")
        footer.classList.remove("light")
    }
    theme_text.textContent = " Dark Mode"
}

function setLight() {
    if (body.classList.contains("dark")) {
        body.classList.remove("dark")
    }
    if (navbar.classList.contains("navbar-dark")) {
        navbar.classList.remove("navbar-dark")
    }
    if (navbar.classList.contains("bg-dark")) {
        navbar.classList.remove("bg-dark")
    } 
    if (econtent.classList.contains("text-light")) {
        econtent.classList.remove("text-light")
    }
    if (!footer.classList.contains("light")) {
        footer.classList.remove("dark")
        footer.classList.add("light")
    }
    theme_text.textContent = " Light Mode"
}

function toggleTheme() {
    if (button.checked) {
        localStorage.setItem("themeSetting", "dark")
        setDark()
        
    } else {
        localStorage.setItem("themeSetting", "light")
        setLight()
    }
}