const menuOpen = document.getElementById('menu-open');
const menuClose = document.getElementById('menu-close');
const sidebar = document.querySelector('.container .sidebar');

menuOpen.addEventListener('click', () => sidebar.style.left = '0');

menuClose.addEventListener('click', () => sidebar.style.left = '-100%');


document.addEventListener('DOMContentLoaded', function() {
    var video = document.getElementById('myVideo');
    video.autoplay = true;
    video.loop = true;
    video.muted = true; // Add this line to mute the video (optional)
});
