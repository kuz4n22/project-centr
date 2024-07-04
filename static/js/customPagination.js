document.addEventListener('DOMContentLoaded', function() {
  var carouselContainers = document.querySelectorAll('.carousel-container');

  carouselContainers.forEach(function(container) {
    var carousel = container.querySelector('.carousel');
    var progressBar = container.querySelector('.pagination-bar');

    var flkty = new Flickity(carousel, {
      freeScroll: false,
      contain: true,
      prevNextButtons: false,
      pageDots: false
    });


    function updateProgressBar() {
      var slidesCount = flkty.slides.length;
      var currentIndex = flkty.selectedIndex;
      var progress = (currentIndex + 1) / slidesCount * 100;
      progressBar.style.width = progress + '%';
    }

    updateProgressBar();

    flkty.on('scroll', function() {
      updateProgressBar();
    });
  });
});