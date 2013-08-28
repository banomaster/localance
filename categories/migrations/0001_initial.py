# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table(u'categories_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('cover_picture', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('cover_picture_thumb', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('title_section_featured', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'categories', ['Category'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table(u'categories_category')


    models = {
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            'cover_picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'cover_picture_thumb': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'title_section_featured': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['categories']