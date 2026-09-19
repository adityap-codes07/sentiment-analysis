let theme = document.getElementById("theme");
let buttonTheme = document.getElementById("themeButton");
let themes = ["/static/dark.css", "/static/light.css", "/static/darkblue.css"];
let savedTheme = Number(localStorage.getItem("sentimentTheme"));
let currentTheme = Number.isInteger(savedTheme) ? savedTheme : 2;

function applyTheme(index) {
    currentTheme = index;
    theme.href = themes[currentTheme];
    localStorage.setItem("sentimentTheme", String(currentTheme));
}

applyTheme(currentTheme);

buttonTheme.addEventListener("click", function () {
    applyTheme((currentTheme + 1) % themes.length);
});