$(document).ready(function() {
	var markup = $('#headerTemplate').html();
	$.template("header", markup);

	markup = $('#createUpdateMetaTemplate').html();
	$.template("createUpdateMeta", markup);

	makeEventInfo();
	// makeAppInfo();
})

function makeEventInfo() {
	$.ajax({
		url: "data/eventInfo.json",
		data: {
			eventId: 0
		},
		type: 'GET',
		dataType: 'json', // added data type
		success: function(res) {

			var string = '<div class="headerLogo" title="' + res.name + '" style="background-image:url(' + res.logo + ')"></div><div class="headerLinks">';

			$(res.links).each(function(index, item) {
				string += '<a href="' + item.url + '"><div class="headerLink">' + item.title + '</div></a>'
			})

			string += '</div>';

			$('#mainContainer .header').html(string);

			string = '<div class="metaBlock"><div class="metaTitle">Relevant Hashtags<m>Click to use</m></div> <div class="metaList">';
			$(res.hashtags).each(function(index, item) {
				string += '<div class="metaListItem">' + item + '</div>'
			})
			string += '</div>\
		</div>\
		<div class="metaBlock">\
			<div class="metaTitle">Relevant Usernames<m>Click to use</m></div>\
			<div class="metaList">';

			$(res.users).each(function(index, item) {
				string += '<div class="metaListItem">' + item + '</div>'
			})

			string += '</div> </div>';

			$('.createUpdateMeta').html(string);
		}
	});
}