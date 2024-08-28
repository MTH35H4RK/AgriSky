document.addEventListener('DOMContentLoaded', () => {
    const themeToggleBtn = document.getElementById('theme-toggle');
    const currentTheme = localStorage.getItem('theme') || 'light';

    if (currentTheme === 'dark') {
        enableDarkMode();
    }

    themeToggleBtn.addEventListener('click', () => {
        if (document.body.classList.contains('dark-mode')) {
            disableDarkMode();
        } else {
            enableDarkMode();
        }
    });

    function enableDarkMode() {
        document.body.classList.add('dark-mode');
        invertColors();
        localStorage.setItem('theme', 'dark');
    }

    function disableDarkMode() {
        document.body.classList.remove('dark-mode');
        revertColors();
        localStorage.setItem('theme', 'light');
    }

    function invertColors() {
        const elements = document.querySelectorAll('*');
        elements.forEach(el => {
            const bgColor = window.getComputedStyle(el).backgroundColor;
            const textColor = window.getComputedStyle(el).color;

            if (bgColor) {
                el.style.backgroundColor = invertColor(bgColor);
            }

            if (textColor) {
                el.style.color = invertColor(textColor);
            }
        });
    }

    function revertColors() {
        const elements = document.querySelectorAll('*');
        elements.forEach(el => {
            el.style.backgroundColor = '';
            el.style.color = '';
        });
    }

    function invertColor(color) {
        const rgb = color.match(/\d+/g);
        if (!rgb) return color;
        const invertedColor = `rgb(${255 - rgb[0]}, ${255 - rgb[1]}, ${255 - rgb[2]})`;
        return invertedColor;
    }
});
