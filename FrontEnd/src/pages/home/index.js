const carousels = document.querySelectorAll('.carousel');
const questions = document.querySelectorAll('.question');
const saibaMaisBtn = document.querySelector('#saiba-mais-btn')

carousels.forEach((carousel) => {
    let currentSlide = 0;
    const slides = carousel.querySelectorAll('.carousel-item');
    const nextButton = carousel.querySelector('.carousel-control.next');
    const prevButton = carousel.querySelector('.carousel-control.prev');

    function showSlide(index) {
        if (index >= slides.length)
            currentSlide = 0;

        else if (index < 0)
            currentSlide = slides.length - 1;
        else
            currentSlide = index;

        slides.forEach((slide) => {
            slide.style.transform = `translateX(-${currentSlide * 100}%)`;
        });
    }

    nextButton.addEventListener('click', () => {
        showSlide(currentSlide + 1);
    });

    prevButton.addEventListener('click', () => {
        showSlide(currentSlide - 1);
    });

    // Initialize the carousel
    showSlide(currentSlide);
});

questions.forEach(question => {
    question.addEventListener('click', () => {
        const answer = question.nextElementSibling;
        const toggleSign = question.querySelector('.toggle-sign');

        if (answer.style.display === 'block') {
            answer.style.display = 'none';
            toggleSign.textContent = '+';
        } else {
            answer.style.display = 'block';
            toggleSign.textContent = '−';
        }
    });
});

saibaMaisBtn.addEventListener('click', () => {
    alert('Página de saiba mais não implementada ainda')
})
