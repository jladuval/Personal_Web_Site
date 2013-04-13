$(document).ready(function() {
	$("img.shakeable").mouseenter(function(){
		$(this).fadeOut(50);
		$(this).fadeIn(500);
	});
});
