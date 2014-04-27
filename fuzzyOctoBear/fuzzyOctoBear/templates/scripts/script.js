$(document).ready(function(){
	var markup = $('#headerTemplate').html();
	$.template("header", markup);

	markup = $('#createUpdateMetaTemplate').html();
	$.template("createUpdateMeta", markup);

	makeEventInfo();
	// makeAppInfo();
})

function makeEventInfo(){
	$.ajax({
		url: "/eventDetails",
		data: {
			eventId: 'osdc'
		},
		type: 'GET',
		dataType: 'json', // added data type
		success: function(res) {
			
			$('#mainContainer .header').html('');
			$.tmpl("header", res).appendTo('#mainContainer .header');

			$('.createUpdateMeta').html('');
			$.tmpl("createUpdateMeta", res).appendTo('.createUpdateMeta');
		}
	});
}