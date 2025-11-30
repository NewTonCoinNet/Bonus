const tg = window.Telegram.WebApp;
tg.expand();

document.getElementById('username').innerText = tg.initDataUnsafe?.user?.username
  ? '@' + tg.initDataUnsafe.user.username
  : 'Гость';

document.getElementById('spin').addEventListener('click', () => {
  const prizes = ['💝 25', '🧸 150', '🌹 100', '🎁 200'];
  const randomPrize = prizes[Math.floor(Math.random() * prizes.length)];
  alert('Ты выиграл: ' + randomPrize);
});