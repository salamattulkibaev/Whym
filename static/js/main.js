$(document).ready(function() {
	var lastScrollPosition = 0;

		$('.btnGoToUp').on("click" ,	 function() {
			if ( $(document).scrollTop() >= 20){
				$('html, body').animate({ scrollTop: 0 }, 10);
				lastScrollPosition = $(document).scrollTop();
			}
			else {
				$('html, body').animate({ scrollTop: lastScrollPosition }, 10);
			}
		});

		$(document).scroll(function(){
			if ($(document).scrollTop() > 0) {
				$('#scroll-up').fadeIn();
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-up fa-2x');
			}else if(lastScrollPosition == 0){
				$('#scroll-up').fadeOut();
			}else{
				$('#scroll-up').find('i').removeClass().addClass('fas fa-angle-down fa-2x');
			}
		});
		
});
