window.onload = function() {
    console.log("heyy");
    const redirectfix = document.getElementsByClassName("redirectcheck")[0];
    if (redirectfix && redirectfix.getAttribute('data-url')) {
        window.location.href = redirectfix.getAttribute('data-url');
    }
};
