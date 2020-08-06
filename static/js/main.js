$(function() {
    $(document).scroll(function() {
        var $nav = $(".navbar-bg");
        $nav.toggleClass('scrolled', $(this).scrollTop() > $nav.height());
    });
});

