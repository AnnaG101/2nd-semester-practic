document.addEventListener('DOMContentLoaded', () => {

    const leftBtn = document.querySelector(".slider__btn-left");
    const rightBtn = document.querySelector(".slider__btn-right");
    const items = document.querySelectorAll(".slider__item");
    let currentIndex = 0;
    
    function resetTransforms() {
        items.forEach((item) => item.style.transform = '');
    }
    
    function nextSlide() {
        resetTransforms();
        items.forEach(element => {
            element.classList.remove("slider__item--active");
        })
        console.log(currentIndex);
        if (currentIndex === items.length - 1) {
            currentIndex = 0;
        } else {
            currentIndex++;
        }
    
        items[currentIndex].classList.add("slider__item--active");
        new Promise(() => {
            setTimeout(() => {
                items[currentIndex].style.transform = 'rotateY(-360deg)';
            }, 10);
        }).then(() => {
            
            items[currentIndex].offsetWidth;
            items[currentIndex].style.transition = 'transform 0.5s linear';
            items[currentIndex].style.transform = '';
        });
    
    }
    
    
    function prevSlide() {
        resetTransforms();
        items.forEach((item) => item.classList.remove('slider__item--active'));
        console.log(currentIndex);
        if (currentIndex === items.length - 1) {
            currentIndex = 0;
        } else {
            currentIndex++;
        }
        
        items[currentIndex].classList.add('slider__item--active');
        new Promise(() => {
            setTimeout(() => {
                items[currentIndex].style.transform = 'rotateY(-360deg)';
    
            }, 10);
        }).then(() => {
    
            items[currentIndex].offsetWidth;
            items[currentIndex].style.transition = 'transform 0.5s linear';
            items[currentIndex].style.transform = '';
        });
    }
    
    leftBtn.addEventListener('click', prevSlide);
    rightBtn.addEventListener('click', nextSlide);
    
    });