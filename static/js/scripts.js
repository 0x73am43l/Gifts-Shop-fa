// 1) Scroll Progress Bar:
// const scrollProgress = document.getElementById('scroll-progress');
// const height =
//   document.documentElement.scrollHeight - document.documentElement.clientHeight;
//
// window.addEventListener('scroll', () => {
//   const scrollTop =
//     document.body.scrollTop || document.documentElement.scrollTop;
//   scrollProgress.style.width = `${(scrollTop / height) * 100}%`;
// });

// 2) Swiper Slider:
// var Swiper;
var swiper = new Swiper(".swiper-container", {
  slidesPerView: 1,
  spaceBetween: 10,
  centeredSlides: true,
  freeMode: true,
  grabCursor: true,
  loop: true,
  pagination: {
    el: ".swiper-pagination",
    clickable: true
  },
  autoplay: {
    delay: 4000,
    disableOnInteraction: false
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev"
  },
  breakpoints: {
    500: {
      slidesPerView: 1
    },
    700: {
      slidesPerView: 1.5
    }
  }
});

// 3) ????:
var triggerTabList = [].slice.call(document.querySelectorAll('#myTab a'))
triggerTabList.forEach(function (triggerEl) {
  var tabTrigger = new bootstrap.Tab(triggerEl)

  triggerEl.addEventListener('click', function (event) {
    event.preventDefault()
    tabTrigger.show()
  })
})

// 4) Protect Against DDoS Attack (prevent F5 after submit)
if (window.history.replaceState){
  window.history.replaceState(null, null, window.location.href);
}