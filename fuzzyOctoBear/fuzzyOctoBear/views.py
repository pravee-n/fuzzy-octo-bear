from django.shortcuts import render
import pdb, json
from fuzzyOctoBear.models import *
from django.http import HttpResponse


def home(request):
	# event = Event()
	# event.name = 'osdConf'
	# event.facebook = 'osdConf'
	# event.twitter = 'osdConf'
	# event.hashtag = 'osdConf'
	# event.primary_color = 'osdConf'
	# event.event_id = 'osdconf'

	# links = []
	# links.append( 'http://osdconf.in' );
	# links.append( 'http://facebook.com/osdconf' );

	# event.save()
	# event = Event.objects.get(id=1)
	# pdb.set_trace()
	return render( request, "index.html" )


{
	"name": "OSDConf 14",
	"logo": "images/logo.png",
	"links": [{
		"title": "Facebook",
		"url": "https://www.facebook.com/groups/jiitlug/"
	}, {
		"title": "Twitter",
		"url": "https://twitter.com/JIITOSDC"
	}],
	"hashtags": ["#OSDConf", "#hacking", "letsHack"],
	"users": ["@osdc", "@OSDConf14"]
}

def eventDetails(request):
	event_id = request.GET['eventId']
	event = Event.objects.get(event_id=event_id)

	res_event = {}
	res_event['name'] = event.name
	res_event['logo'] = ''
	res_event['facebook'] = event.facebook
	res_event['twitter'] = event.twitter
	res_event['hashtag'] = ["#OSDConf", "#hacking", "letsHack"]
	res_event['users'] = ["@osdc", "@OSDConf14"]


	links = []
	link = {}
	link['title'] = 'Facebook'
	link['url'] = "https://www.facebook.com/groups/jiitlug/"

	links.append(link)

	link['title'] = 'Twitter'
	link['url'] = "https://www.twitter.com/JIITOSDC"

	links.append(link)

	res_event['links'] = links

	return HttpResponse(json.dumps(res_event), content_type="application/json")


def hello(request):
	return render( request, "home.html" )