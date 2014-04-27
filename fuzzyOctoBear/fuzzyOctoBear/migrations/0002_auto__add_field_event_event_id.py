# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Event.event_id'
        db.add_column(u'fuzzyOctoBear_event', 'event_id',
                      self.gf('django.db.models.fields.CharField')(max_length=20, null=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Event.event_id'
        db.delete_column(u'fuzzyOctoBear_event', 'event_id')


    models = {
        u'fuzzyOctoBear.event': {
            'Meta': {'object_name': 'Event'},
            'event_id': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True'}),
            'facebook': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'hashtag': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'links': ('django.db.models.fields.CharField', [], {'max_length': '5000'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'primary_color': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['fuzzyOctoBear']