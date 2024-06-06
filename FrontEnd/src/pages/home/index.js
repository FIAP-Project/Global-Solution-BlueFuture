const carousels = document.querySelectorAll('.carousel');

const saibaMaisBtn = document.querySelector('#saiba-mais-btn')

const questions = document.querySelectorAll('.question');

const participeBtn = document.querySelector('#participe-btn')
const popup = document.getElementById("popup");
const closePopupButton = document.getElementById("closePopup");

const form = document.querySelector('#createAccountForm')

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

participeBtn.addEventListener("click", () => {
    popup.style.display = "block";
    document.body.classList.add("no-scroll");
});

closePopupButton.addEventListener("click", () => {
    popup.style.display = "none";
    document.body.classList.remove("no-scroll");
});

form.addEventListener('submit', (e) => {
    e.preventDefault()

    let valid = true;

    const name = document.getElementById("nome").value;
    const email = document.getElementById("email").value;
    const tel = document.getElementById("telefone").value;

    if (!validName(name) || !validEmail(email) || !validTel(tel))
        valid = false

    if (valid)
        form.submit();
})

function validName(name) {
    if (name.length < 3) {
        alert("Name must be at least 3 characters long");
        return false;
    }
    return true
}

function validEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        alert("Invalid email address")
        return false;
    }
    return true
}

function validTel(tel) {
    const telPattern = /^\d{2} \d{5}-\d{4}$/;
    if (!telPattern.test(tel)) {
        alert("Invalid phone number format. Use 99 99999-9999");
        return false;
    }
    return true
}