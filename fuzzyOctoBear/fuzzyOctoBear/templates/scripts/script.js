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
		url: "data/eventInfo.json",
		data: {
			eventId: 0
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