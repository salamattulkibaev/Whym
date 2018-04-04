$(document).ready(function() {
	var lastScrollPosition = 0;

		$('.left').on("click" ,	 function() {
			if ( $(window).scrollTop() >= 20){
				$('html, body').animate({ scrollTop: 0 }, 10);
				lastScrollPosition = $(window).scrollTop();
			}
			else {
					history.back();
			}
		});

		$('#scroll-up').fadeIn();
		$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-left fa-2x');
		$(window).scroll(function(){
			if ($(window).scrollTop() != 0) {
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-up fa-2x');
			}
			else{
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-left fa-2x');
			}
		});

		$(".comment-reply-btn").click(function (event) {
			event.preventDefault();
			$(this).parent().parent().next(".comment-reply").fadeToggle();
        });
});
