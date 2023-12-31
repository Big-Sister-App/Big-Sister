//  Navbar Scroll Js
$(window).scroll(function() {
  $('nav').toggleClass('scrolled', $(this).scrollTop() > 50);
});


// Navbar Scroll Spy Js
$(document).ready(function() {
  const sectionIds = $('a.nav-link');
  $(document).scroll(function() {
    sectionIds.each(function() {
      const container = $(this).attr('href');
      const containerOffset = $(container).offset().top;
      const containerHeight = $(container).outerHeight();
      const containerBottom = containerOffset + containerHeight;
      const scrollPosition = $(document).scrollTop();
      if (scrollPosition < containerBottom - 350 &&
        scrollPosition >= containerOffset - 350) {
        $(this).addClass('active');
      } else {
        $(this).removeClass('active');
      }
    });
  });
});


// Navbar Link Js
$('.nav-link').on('click', function() {
  $('.nav-link').removeClass('active');
  $(this).addClass('active');
});

$('.nav-link, .vvd ').on('click', function() {
  $('.navbar-collapse').collapse('hide');
});


// Skill Slider Js
$('.skill-slider').owlCarousel({
  loop: true,
  margin: 10,
  nav: true,
  navText: ['<img src=\'/static/images/arrow1.svg\'>',
    '<img src=\'/static/images/arrow2.svg\'>'],
  dots: false,
  responsive: {
    0: {
      items: 1,
    },
    575: {
      items: 2,
    },
    768: {
      items: 3,
    },
  },
});


// Text Animate JS
const TxtRotate = function(el, toRotate, period) {
  this.toRotate = toRotate;
  this.el = el;
  this.loopNum = 0;
  this.period = parseInt(period, 10) || 2000;
  this.txt = '';
  this.tick();
  this.isDeleting = false;
};

TxtRotate.prototype.tick = function() {
  const i = this.loopNum % this.toRotate.length;
  const fullTxt = this.toRotate[i];

  if (this.isDeleting) {
    this.txt = fullTxt.substring(0, this.txt.length - 1);
  } else {
    this.txt = fullTxt.substring(0, this.txt.length + 1);
  }

  this.el.innerHTML = '<span class="wrap">'+this.txt+'</span>';

  const that = this;
  let delta = 300 - Math.random() * 100;

  if (this.isDeleting) {
    delta /= 2;
  }

  if (!this.isDeleting && this.txt === fullTxt) {
    delta = this.period;
    this.isDeleting = true;
  } else if (this.isDeleting && this.txt === '') {
    this.isDeleting = false;
    this.loopNum++;
    delta = 500;
  }

  setTimeout(function() {
    that.tick();
  }, delta);
};

window.onload = function() {
  const elements = document.getElementsByClassName('txt-rotate');
  for (let i=0; i<elements.length; i++) {
    const toRotate = elements[i].getAttribute('data-rotate');
    const period = elements[i].getAttribute('data-period');
    if (toRotate) {
      new TxtRotate(elements[i], JSON.parse(toRotate), period);
    }
  }
  // INJECT CSS
  const css = document.createElement('style');
  css.type = 'text/css';
  css.innerHTML = '.txt-rotate > .wrap { border-right: 0.08em solid #666 }';
  document.body.appendChild(css);
};

// WOW Animation JS
wow = new WOW(
    {
      boxClass: 'wow', // default
      animateClass: 'animated', // change this if you are not using animate.css
      offset: 0, // default
      mobile: true, // keep it on mobile
      live: true, // track if element updates
    },
);
wow.init();


