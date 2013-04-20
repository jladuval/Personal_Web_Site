$(function() {

	var latlng = new google.maps.LatLng(-43.531874,172.63504);
	var settings = {
		zoom: 10,
		scrollwheel: false,
		center: latlng,
		mapTypeControl: true,
		mapTypeControlOptions: {style: google.maps.MapTypeControlStyle.DROPDOWN_MENU},
		navigationControl: true,
		navigationControlOptions: {style: google.maps.NavigationControlStyle.SMALL},
		mapTypeId: google.maps.MapTypeId.ROADMAP};
	var map = new google.maps.Map(document.getElementById("map_canvas"), settings);
	var contentString = '<div style="color: black">'+
		'<h4>Jacob Duval</h4>'+
		'</div>';
	var infowindow = new google.maps.InfoWindow({
		content: contentString
	});
	
	

});