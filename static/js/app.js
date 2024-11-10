function toggleMenu() {
    const menu = document.getElementById('menu');
    const hamburger = document.getElementById('hamburger');

    // Переключение видимости меню
    if (menu.style.visibility === 'visible') {
        menu.style.opacity = '0';
        menu.style.transform = 'translateY(-100%)'; // Скрыть меню
        setTimeout(() => {
            menu.style.visibility = 'hidden'; // Установить видимость в hidden после анимации
        }, 1000); // Задержка на время анимации
    } else {
        menu.style.visibility = 'visible';
        setTimeout(() => {
            menu.style.opacity = '1';
            menu.style.transform = 'translateY(0)'; // Показать меню
        }, 0); // Устанавливаем transform сразу после изменения visibility
    }

    // Переключение классов для гамбургера
    hamburger.classList.toggle('active');
}

function closeMenu() {
    const menu = document.getElementById('menu');
    const hamburger = document.getElementById('hamburger');

    // Скрыть меню
    menu.style.display = 'none';

    // Удалить класс активности у гамбургера
    hamburger.classList.remove('active');
}

// Добавление обработчиков событий для элементов меню
document.querySelectorAll('.menu a').forEach(item => {
    item.addEventListener('click', closeMenu);
});
