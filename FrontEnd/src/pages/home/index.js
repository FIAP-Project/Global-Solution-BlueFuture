document.addEventListener('DOMContentLoaded', () => {
    const carousels = document.querySelectorAll('.carousel');

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
});
