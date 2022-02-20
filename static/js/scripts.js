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

// 5) Porfile Picture
var loadFile = function (event) {
  var image = document.getElementById("output");
  image.src = URL.createObjectURL(event.target.files[0]);
};

// 5) Protect Against DDoS Attack (prevent F5 after submit)
if (window.history.replaceState){
  window.history.replaceState(null, null, window.location.href);
}

 // 6) OTP Number Input
document.addEventListener("DOMContentLoaded", function(event) {
    var input = document.getElementById('first');
    input.focus();
    function OTPInput() {
        const inputs = document.querySelectorAll('#otp > *[id]');
        for (let i = 0; i < inputs.length; i++) {
            inputs[i].addEventListener('keydown', function(event) {
                if (event.key==="Backspace" ) {
                    inputs[i].value='' ; if (i !==0) inputs[i - 1].focus();
                } else { if (i===inputs.length - 1 && inputs[i].value !=='' ) {
                    return true;
                } else if ((event.keyCode> 47 && event.keyCode < 58) ||  (event.keyCode >= 96 && event.keyCode <= 105)){
                    inputs[i].value=event.key; if (i !==inputs.length - 1) inputs[i + 1].focus(); event.preventDefault();
                }
                // else if (event.keyCode> 64 && event.keyCode < 91) {
                //     inputs[i].value=String.fromCharCode(event.keyCode); if (i !==inputs.length - 1) inputs[i + 1].focus(); event.preventDefault();
                // }
                }
            });
        } } OTPInput();
});

// Some random colors
const colors = ["#3CC157", "#2AA7FF", "#1B1B1B", "#FCBC0F", "#F85F36"];

const numBalls = 20;
const balls = [];

for (let i = 0; i < numBalls; i++) {
  let ball = document.createElement("div");
  ball.classList.add("ball");
  ball.style.background = colors[Math.floor(Math.random() * colors.length)];
  ball.style.left = `${Math.floor(Math.random() * 100)}vw`;
  ball.style.top = `${Math.floor(Math.random() * 100)}vh`;
  ball.style.transform = `scale(${Math.random()})`;
  ball.style.width = `${Math.random()}em`;
  ball.style.height = ball.style.width;

  balls.push(ball);
  document.body.append(ball);
}

// Keyframes
balls.forEach((el, i, ra) => {
  let to = {
    x: Math.random() * (i % 2 === 0 ? -11 : 11),
    y: Math.random() * 12
  };

  let anim = el.animate(
    [
      { transform: "translate(0, 0)" },
      { transform: `translate(${to.x}rem, ${to.y}rem)` }
    ],
    {
      duration: (Math.random() + 1) * 12000, // random duration
      direction: "alternate",
      fill: "both",
      iterations: Infinity,
      easing: "ease-in-out"
    }
  );
});
