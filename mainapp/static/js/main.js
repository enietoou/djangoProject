//Scroll to top
$(document).ready(function() {
    // Отслеживаем событие прокрутки
    $(window).scroll(function() {
        if ($(this).scrollTop() > 100) {
            // Если прокрутка больше 100 пикселей, показываем кнопку
            $('#scroll-to-top').fadeIn();
        } else {
            // Иначе скрываем кнопку
            $('#scroll-to-top').fadeOut();
        }
    });

    // Обработчик клика на кнопке
    $('#scroll-to-top').click(function() {
        // Плавно прокручиваем наверх
        $('html, body').animate({scrollTop: 0}, 800);
        return false;
    });
});