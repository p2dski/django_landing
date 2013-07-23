# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Join.zip_code'
        db.add_column(u'join_join', 'zip_code',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Join.zip_code'
        db.delete_column(u'join_join', 'zip_code')


    models = {
        u'join.join': {
            'Meta': {'object_name': 'Join'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '250'}),
            'full_name': ('django.db.models.fields.CharField', [], {'max_length': '250', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'zip_code': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['join']