document.addEventListener('DOMContentLoaded', function() {
    // Initialize WOW.js
    new WOW().init();

    // Fact Section: Number Counter Animation
    const counters = document.querySelectorAll('.counter-number');
    counters.forEach(counter => {
        const target = parseInt(counter.getAttribute('data-value'));
        let current = 0;
        const increment = Math.ceil(target / 10); // 50 steps
        const duration = 4000; // 1 second
        const stepTime = duration / (target / increment);

        const updateCounter = () => {
            current += increment;
            if (current >= target) {
                counter.textContent = target;
                return;
            }
            counter.textContent = current;
            setTimeout(updateCounter, stepTime);
        };

        // Trigger when counter is in view
        const observer = new IntersectionObserver(
            (entries) => {
                if (entries[0].isIntersecting) {
                    updateCounter();
                    observer.disconnect();
                }
            },
            { threshold: 0.1 }
        );
        observer.observe(counter);
    });

    // Testimonial Section: Custom Carousel
    const track = document.querySelector('.carousel-track');
    const cards = document.querySelectorAll('.testimonial-card');
    const prevBtn = document.querySelector('.carousel-prev');
    const nextBtn = document.querySelector('.carousel-next');

    // Clone cards for continuous loop
    const totalCards = cards.length;
    for (let i = 0; i < totalCards; i++) {
        const clone = cards[i].cloneNode(true);
        track.appendChild(clone);
    }

    // Update card widths based on screen size
    const updateCardWidths = () => {
        const allCards = document.querySelectorAll('.testimonial-card'); // Include clones
        const cardWidth = window.innerWidth >= 1000 ? (track.parentElement.offsetWidth / 3 - 20) :
                         window.innerWidth >= 768 ? (track.parentElement.offsetWidth / 2 - 20) :
                         (track.parentElement.offsetWidth - 20); // 1 card on small screens
        allCards.forEach(card => {
            card.style.flex = `0 0 ${cardWidth}px`;
            card.style.maxWidth = `${cardWidth}px`;
        });
    };

    // Initial width setup
    updateCardWidths();

    // Handle navigation
    let currentIndex = 0;
    const cardWidth = cards[0].offsetWidth + 20; // Include margin
    const maxIndex = totalCards; // Original cards count

    const updateCarousel = () => {
        const offset = -currentIndex * cardWidth;
        track.style.transform = `translateX(${offset}px)`;
        // Reset to start for continuous loop
        if (currentIndex >= maxIndex) {
            setTimeout(() => {
                track.style.transition = 'none';
                currentIndex = 0;
                track.style.transform = `translateX(0)`;
                setTimeout(() => {
                    track.style.transition = 'transform 0.5s ease-in-out';
                }, 50);
            }, 500); // Match transition duration
        }
    };

    const moveToNext = () => {
        currentIndex++;
        track.style.transition = 'transform 0.5s ease-in-out';
        updateCarousel();
    };

    const moveToPrev = () => {
        if (currentIndex === 0) {
            // Jump to end for continuous loop
            track.style.transition = 'none';
            currentIndex = maxIndex;
            track.style.transform = `translateX(${-currentIndex * cardWidth}px)`;
            setTimeout(() => {
                track.style.transition = 'transform 0.5s ease-in-out';
                currentIndex--;
                updateCarousel();
            }, 50);
        } else {
            currentIndex--;
            updateCarousel();
        }
    };

    nextBtn.addEventListener('click', moveToNext);
    prevBtn.addEventListener('click', moveToPrev);

    // Auto-play (optional, since CSS handles continuous scrolling)
    let autoPlay = setInterval(moveToNext, 4000);
    track.addEventListener('mouseenter', () => clearInterval(autoPlay));
    track.addEventListener('mouseleave', () => autoPlay = setInterval(moveToNext, 4000));

    // Update card widths on resize
    window.addEventListener('resize', updateCardWidths);

    // Debug Logs
    console.log('Index.html: Counter numbers found:', counters.length);
    if (counters.length === 0) {
        console.error('Index.html: Counter numbers not found!');
    }

    console.log('Index.html: Testimonial cards found:', cards.length);
    if (cards.length === 0) {
        console.error('Index.html: Testimonial carousel not found!');
    } else {
        console.log('Index.html: Custom carousel initialized');
    }
});