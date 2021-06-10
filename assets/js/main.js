/*-----------------------------------------------------------------------------------

    Theme Name: Live - Multipurpose Blog Template
    Description: Multipurpose Blog Template
    Author: Chitrakoot Web
    Version: 1.0

    /* ----------------------------------

    JS Active Code Index

        01. Preloader
        02. Header class - on scroll
        03. Scroll To Top
        04. Parallax
        05. Resize function
        06. FullScreenHeight function
        07. ScreenFixedHeight function
        08. FullScreenHeight and screenHeight with resize function
        09. Sliders
        10. Gallery
        11. Stellar

    ---------------------------------- */


(function($) {

    "use strict";

    var $window = $(window);


        /*------------------------------------
            01. Preloader
        --------------------------------------*/

        $('#preloader').fadeOut('normall', function() {
            $(this).remove();
        });

        /*------------------------------------
            02. Header class - on scroll
        --------------------------------------*/

        $window.on('scroll', function() {
            var scroll = $window.scrollTop();
            if (scroll <= 50) {
                $("header").removeClass("scrollHeader").addClass("fixedHeader");
            }
            else {
                $("header").removeClass("fixedHeader").addClass("scrollHeader");
            }
        });

        /*------------------------------------
            03. Scroll To Top
        --------------------------------------*/

        $window.on('scroll', function() {
            if ($(this).scrollTop() > 500) {
                $(".scroll-to-top").fadeIn(400);

            } else {
                $(".scroll-to-top").fadeOut(400);
            }
        });

        $(".scroll-to-top").on('click', function(event) {
            event.preventDefault();
            $("html, body").animate({
                scrollTop: 0
            }, 600);
        });

        /*------------------------------------
            04. Parallax
        --------------------------------------*/

        // sections background image from data background
        var pageSection = $(".parallax,.bg-img");
        pageSection.each(function(indx) {

            if ($(this).attr("data-background")) {
                $(this).css("background-image", "url(" + $(this).data("background") + ")");
            }
        });


        /*------------------------------------
            05. Resize function
        --------------------------------------*/

        $window.resize(function(event) {
            setTimeout(function() {
                SetResizeContent();
            }, 500);
            event.preventDefault();
        });


        /*------------------------------------
            06. FullScreenHeight function
        --------------------------------------*/

        function fullScreenHeight() {
            var element = $(".full-screen");
            var $minheight = $window.height();
            element.css('min-height', $minheight);
        }


        /*------------------------------------
            07. ScreenFixedHeight function
        --------------------------------------*/

        function ScreenFixedHeight() {
            var $headerHeight = $("header").height();
            var element = $(".screen-height");
            var $screenheight = $window.height() - $headerHeight;
            element.css('height', $screenheight);
        }


        /*------------------------------------
            08. FullScreenHeight and screenHeight with resize function
        --------------------------------------*/

        function SetResizeContent() {
            fullScreenHeight();
            ScreenFixedHeight();
        }

        SetResizeContent();

    // === when document ready === //
    $(document).on("ready", function() {


        /*------------------------------------
            09. Sliders
        --------------------------------------*/

        // Testmonials carousel1
        $('#testmonials-carousel').owlCarousel({
            loop: true,
            responsiveClass: true,
            autoplay: true,
            smartSpeed: 800,
            nav: false,
            dots: true,
            center:false,
            margin: 0,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 1
                },
                992: {
                    items: 1
                }
            }
        });

        // Testmonials carousel1
        $('#trending-carousel').owlCarousel({
            loop: true,
            responsiveClass: true,
            autoplay: true,
            smartSpeed: 800,
            nav: false,
            dots: false,
            center:false,
            margin: 30,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                992: {
                    items: 4
                }
            }
        });

        // Testmonials carousel1
        $('#portfolio-carousel').owlCarousel({
            loop: true,
            responsiveClass: true,
            autoplay: true,
            smartSpeed: 800,
            nav: false,
            dots: false,
            center:false,
            margin: 0,
            responsive: {
                0: {
                    items: 1
                },
                576: {
                    items: 2
                },
                768: {
                    items: 3
                },
                992: {
                    items: 5
                }
            }
        });

        // Testmonials carousel1
        $('#banner-carousel').owlCarousel({
            loop: true,
            responsiveClass: true,
            autoplay: true,
            smartSpeed: 800,
            nav: false,
            dots: false,
            center:true,
            margin: 5,
            responsive: {
                0: {
                    items: 1
                },
                768: {
                    items: 2
                },
                992: {
                    items: 3
                }
            }
        });

        // Default owlCarousel
        $('.owl-carousel').owlCarousel({
            items: 1,
            loop:true,
            dots: true,
            margin: 0,
            autoplay:true,
            smartSpeed:500
        });


        /*------------------------------------
            10. Gallery
        --------------------------------------*/

        // magnificPopup
        if ($(".gallery").length !== 0) {
            $('.gallery').magnificPopup({
                delegate: '.popimg',
                type: 'image',
                gallery: {
                    enabled: true
                }
            });
        }

        // isotope
        if ($(".gallery").length !== 0) {
            var $gallery = $('.gallery').isotope({
                // options
            });
        }

        // magnificPopup
        if ($(".gallery-post").length !== 0) {
            $('.gallery-post').magnificPopup({
                delegate: '.popimg',
                type: 'image',
                gallery: {
                    enabled: true
                }
            });
        }

        // video
        $('.story-video').magnificPopup({
            delegate: '.video',
            type: 'iframe'
        });

        // filter items on button click
        $('.filtering').on('click', 'span', function() {
            var filterValue = $(this).attr('data-filter');
            $gallery.isotope({
                filter: filterValue
            });
        });

        $('.filtering').on('click', 'span', function() {
            $(this).addClass('active').siblings().removeClass('active');
        });

    });

    // === when window loading === //
    $window.on("load", function() {

        /*------------------------------------
            11. Stellar
        --------------------------------------*/

        // stellar
        $window.stellar();

    });

})(jQuery);
