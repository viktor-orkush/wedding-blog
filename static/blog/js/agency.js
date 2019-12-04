/*Owl Carousel 2*/

$('.owl-carousel').owlCarousel({
    // nav:true, // Show next and prev buttons
    paddingLeft: 200,
    autoplaySpeed: 300,
    navSpeed: 400,
    items: 1,
    loop: true,
    center: true,
})

/*END Owl Carousel 2*/

// gallery
$(function () {
    var selectedClass = "";
    $(".filter").click(function () {
        selectedClass = $(this).attr("data-rel");
        $("#gallery").fadeTo(100, 0.1);
        $("#gallery div").not("." + selectedClass).fadeOut().removeClass('animation');
        setTimeout(function () {
            $("." + selectedClass).fadeIn().addClass('animation');
            $("#gallery").fadeTo(300, 1);
        }, 300);
    });
});
// END gallery

// Тип Image - галерея картинок
$('.popup-gallery').magnificPopup({
    delegate: 'a',
    type: 'image',
    tLoading: 'Загрузка изображения #%curr%...',
    mainClass: 'mfp-img-mobile',
    image: {
        verticalFit: true,
        titleSrc: function (item) {
            return item.el.attr('title') + ' &middot; <a class="image-source-link" href="' + item.el.attr('data-source') + '" target="_blank">image source</a>';
        }
    },
    gallery: {
        enabled: true,
        navigateByImgClick: true,
        preload: [0, 1] // Will preload 0 - before current, and 1 after the current image
    },
    zoom: {
        enabled: true,
        duration: 300, // don't foget to change the duration also in CSS
        opener: function (element) {
            return element.find('img');
        }
    }
});

// endgallery


(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: (target.offset().top - 54)
                }, 1000, "easeInOutExpo");
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 56
    });

    // Collapse Navbar
    var navbarCollapse = function () {
        if ($("#mainNav").offset().top > 100) {
            $("#mainNav").addClass("navbar-shrink");
        } else {
            $("#mainNav").removeClass("navbar-shrink");
        }
    };
    // Collapse now if page is not at top
    navbarCollapse();
    // Collapse the navbar when page is scrolled
    $(window).scroll(navbarCollapse);

})(jQuery); // End of use strict






$(document).ready(function() {
	$('.zoom-gallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		closeOnContentClick: false,
		closeBtnInside: false,
		mainClass: 'mfp-with-zoom mfp-img-mobile',
		image: {
			verticalFit: true,
			titleSrc: function(item) {
				return item.el.attr('title') + ' &middot; <a class="image-source-link" href="'+item.el.attr('data-source')+'" target="_blank">image source</a>';
			}
		},
		gallery: {
			enabled: true
		},
		zoom: {
			enabled: true,
			duration: 300, // don't foget to change the duration also in CSS
			opener: function(element) {
				return element.find('img');
			}
		}

	});
});
