try {

    var fullAnimation = (function () {
    
    
        var colouredRectangles = anime.timeline({
            targets: '.hero-figure-box-01, .hero-figure-box-02, .hero-figure-box-03, .hero-figure-box-04, .hero-figure-box-08, .hero-figure-box-09, .hero-figure-box-10',
            autoplay: false
        }).add({
            duration: anime.random(600, 800),
            delay: anime.random(600, 800),
            rotate: [anime.random(-360, 360), function (el) { return el.getAttribute('data-rotation') }],
            scale: [0.7, 1],
            opacity: [0, 1],
            easing: 'easeInOutExpo'
        });
    
        function init() {
            setTimeout(function () {
                colouredRectangles.play();
            }, 200);
        }
    
    
        function seek() {
            colouredRectangles.seek(colouredRectangles.duration * (1000 / 100));
        }
    
        return {
            init: init,
            seek: seek
        };
    })()
    
    // Start on load
    window.onload = function () {
        fullAnimation.init();
    };
    
    
    // Seek
    var seekProgressEl = document.querySelector('.progress');
    seekProgressEl.addEventListener('input', function () {
        fullAnimation.seek();
    });
}catch {
    
}