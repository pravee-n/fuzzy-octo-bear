# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Event'
        db.create_table(u'fuzzyOctoBear_event', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('facebook', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('hashtag', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('links', self.gf('django.db.models.fields.CharField')(max_length=5000)),
            ('primary_color', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'fuzzyOctoBear', ['Event'])


    def backwards(self, orm):
        # Deleting model 'Event'
        db.delete_table(u'fuzzyOctoBear_event')


    models = {
        u'fuzzyOctoBear.event': {
            'Meta': {'object_name': 'Event'},
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