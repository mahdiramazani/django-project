


$('.show_news_owl_carousel').owlCarousel({
    loop: true,
    nav: true,
    autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
    navText: ["<i class='fa fa-angle-right'></i>", "<i class='fa fa-angle-left'></i>"],
    responsive: {0: {items: 1}, 600: {items: 2}, 1000: {items: 3}}
});

$('.show_news_owl_carousel2').owlCarousel({
    loop: true,
    nav: true,
    autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
    navText: ["<i class='fa fa-angle-right'></i>", "<i class='fa fa-angle-left'></i>"],
    responsive: {0: {items: 1}, 600: {items: 1}, 1000: {items: 1}}
});
$('.show_news_owl_carousel4').owlCarousel({
    loop: true,
    nav: false,
    dots:true,
    autoplay:true,
    autoplayTimeout:2000,
    autoplayHoverPause:true,
    navText: ["<i class='fa fa-angle-right'></i>", "<i class='fa fa-angle-left'></i>"],
    responsive: {0: {items: 1}, 600: {items: 1}, 1000: {items: 1}}
});

function scroll_top() {
    $("html,body").animate({
        scrollTop: "0px"
    }, 1000, "swing");
}

// Script For Fix Header on Scroll
$(window).on('scroll', function() {
    var scroll = $(window).scrollTop();

    if (scroll >= 50) {
        $(".header").addClass("sticky-shadow");
    } else {
        $(".header").removeClass("sticky-shadow");
    }
});