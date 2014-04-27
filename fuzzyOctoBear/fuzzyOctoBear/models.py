from django.db import models

class Event( models.Model ):
	name = models.CharField(max_length=200)
	facebook = models.CharField(max_length=200)
	twitter = models.CharField(max_length=200)
	hashtag = models.CharField(max_length=200)
	links = models.CharField(max_length=5000)
	primary_color = models.CharField(max_length=20)
	event_id = models.CharField(max_length=20, null=True)