const openPopupButton = document.getElementById('openPopup');
const closePopupButton = document.getElementById('closePopup');
const popup = document.getElementById('popup');
const feedFrame = document.getElementById('feedFrame');

openPopupButton.addEventListener('click', () => {
  const feedUrl = 'URL_OF_YOUR_FEED_HERE'; // Replace with the URL you want to display
  feedFrame.src = feedUrl;
  popup.style.display = 'block';
});

closePopupButton.addEventListener('click', () => {
  feedFrame.src = '';
  popup.style.display = 'none';
});
