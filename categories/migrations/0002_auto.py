# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding M2M table for field cities on 'Category'
        m2m_table_name = db.shorten_name(u'categories_category_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('category', models.ForeignKey(orm[u'categories.category'], null=False)),
            ('city', models.ForeignKey(orm[u'cities.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['category_id', 'city_id'])


    def backwards(self, orm):
        # Removing M2M table for field cities on 'Category'
        db.delete_table(db.shorten_name(u'categories_category_cities'))


    models = {
        u'categories.category': {
            'Meta': {'object_name': 'Category'},
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.City']", 'symmetrical': 'False'}),
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
        },
        u'cities.city': {
            'Meta': {'object_name': 'City'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'})
        }
    }

    complete_apps = ['categories']