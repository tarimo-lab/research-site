(function ($) {
    "use strict";
    $.fn.menumaker = function (options) {

        var nav = $(this),

            settings = $.extend({
                format: "dropdown",
                sticky: false
            }, options);

        return this.each(function () {

            $(this).find(".navbar-toggler").on('click', function () {
                $(this).toggleClass('menu-opened');
                var mainmenu = $(this).next('ul');
                if (mainmenu.hasClass('open')) {
                    mainmenu.slideToggle().removeClass('open');
                } else {
                    mainmenu.slideToggle().addClass('open');
                    if (settings.format === "dropdown") {
                        mainmenu.find('ul').show();
                    }
                }
            });

            nav.find('.navbar-nav li ul').parent().addClass('has-sub');
            nav.find('.navbar-nav li ul li').parent().addClass('sub-menu');
            var multiTg = function () {

                // For First Level
                nav.find(".has-sub").prepend('<span class="submenu-button"></span>');
                nav.find('.navbar-nav > li.has-sub > .submenu-button').on('click', function () {
                    $(this).next('.sub-menu').slideToggle();
                    $(this).siblings('ul').addClass('open').slideToggle();
                    $(this).parents('.navbar-nav > li.has-sub').toggleClass('active').siblings('.has-sub').children('.sub-menu').slideUp().removeClass('open').parents('li').removeClass('active');
                });

                // For Second Level
                nav.find('.sub-menu > li.has-sub > .submenu-button').on('click', function () {
                    $(this).next('.sub-menu').slideToggle();
                    $(this).siblings('ul').addClass('open').slideToggle();
                    $(this).parents('.sub-menu > li').toggleClass('active').siblings('.has-sub').children('.sub-menu').slideUp().removeClass('open').parents('li').removeClass('active');
                    if ($(this).siblings('ul').hasClass('open')) {
                        $(this).parents('li').eq(1).addClass('active');
                    }
                });

            };

            if (settings.format === 'multitoggle') multiTg();
            else nav.addClass('dropdown');
            if (settings.sticky === true) nav.css('position', 'fixed');
            var resizeFix = function () {
                var mediasize = 991;
                if ($(window).width() > mediasize) {
                    nav.find('ul').show();
                }
            };

            resizeFix();
            return $(window).on('resize', resizeFix);

        });
    };

    $(document).ready(function () {

        $("nav").menumaker({
            format: "multitoggle"
        });

        /*------------------------------------
            Menu Selector
        --------------------------------------*/

        var urlparam = window.location.pathname.split('/');
        var menuselctor = window.location.pathname;
        if (urlparam[urlparam.length - 1].length > 0) menuselctor = urlparam[urlparam.length - 1];
        else menuselctor = urlparam[urlparam.length - 2];
        $('.navbar-nav li').find('a[href="' + menuselctor + '"]').closest('li').addClass('active').parents().eq(1).addClass('current');
        $('.navbar-nav li.has-sub ul li').find('a[href="' + menuselctor + '"]').parents().eq(4).addClass('current');
    });

    /*------------------------------------
            Toggle Search
    --------------------------------------*/

    $(".navbar-default .attr-nav").each(function () {
        $("li.search > a", this).on("click", function (e) {
            e.preventDefault();
            $(".top-search").slideToggle();
        });
    });

    $(".input-group-addon.close-search").on("click", function () {
        $(".top-search").slideUp();
    });

})(jQuery);