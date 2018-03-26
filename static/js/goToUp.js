$(document).ready(function() {
	var lastScrollPosition = 0;

		$('.left').on("click" ,	 function() {
			if ( $(window).scrollTop() >= 20){
				$('html, body').animate({ scrollTop: 0 }, 10);
				lastScrollPosition = $(window).scrollTop();
			}
			else {
				$('html, body').animate({ scrollTop: lastScrollPosition }, 10);
			}
		});

		$(window).scroll(function(){
			if ($(window).scrollTop() != 0) {
				$('#scroll-up').fadeIn();
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-up fa-2x');
			}else if(lastScrollPosition == 0){
				$('#scroll-up').fadeOut();
			}else{
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-down fa-2x');
			}
		});


		
});
