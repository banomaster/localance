# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ListPhotographerSkills'
        db.create_table(u'photographers_listphotographerskills', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('skill', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'photographers', ['ListPhotographerSkills'])

        # Adding model 'ListPhotographerClients'
        db.create_table(u'photographers_listphotographerclients', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('client', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'photographers', ['ListPhotographerClients'])

        # Adding model 'Photographer'
        db.create_table(u'photographers_photographer', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('name', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['accounts.UserAccount'], unique=True)),
            ('nickname', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(default='', max_length=255, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')()),
            ('tagline', self.gf('django.db.models.fields.TextField')()),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(default=3, to=orm['categories.Category'])),
            ('personal_website', self.gf('django.db.models.fields.URLField')(max_length=40, blank=True)),
            ('available', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('twitter_profile', self.gf('django.db.models.fields.URLField')(max_length=40, blank=True)),
            ('linkedin_profile', self.gf('django.db.models.fields.URLField')(max_length=50, blank=True)),
            ('featured_in_category', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('picture_portfolio', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'photographers', ['Photographer'])

        # Adding M2M table for field cities on 'Photographer'
        m2m_table_name = db.shorten_name(u'photographers_photographer_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photographer', models.ForeignKey(orm[u'photographers.photographer'], null=False)),
            ('city', models.ForeignKey(orm[u'cities.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photographer_id', 'city_id'])

        # Adding M2M table for field clients on 'Photographer'
        m2m_table_name = db.shorten_name(u'photographers_photographer_clients')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photographer', models.ForeignKey(orm[u'photographers.photographer'], null=False)),
            ('listphotographerclients', models.ForeignKey(orm[u'photographers.listphotographerclients'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photographer_id', 'listphotographerclients_id'])

        # Adding M2M table for field skills on 'Photographer'
        m2m_table_name = db.shorten_name(u'photographers_photographer_skills')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('photographer', models.ForeignKey(orm[u'photographers.photographer'], null=False)),
            ('listphotographerskills', models.ForeignKey(orm[u'photographers.listphotographerskills'], null=False))
        ))
        db.create_unique(m2m_table_name, ['photographer_id', 'listphotographerskills_id'])


    def backwards(self, orm):
        # Deleting model 'ListPhotographerSkills'
        db.delete_table(u'photographers_listphotographerskills')

        # Deleting model 'ListPhotographerClients'
        db.delete_table(u'photographers_listphotographerclients')

        # Deleting model 'Photographer'
        db.delete_table(u'photographers_photographer')

        # Removing M2M table for field cities on 'Photographer'
        db.delete_table(db.shorten_name(u'photographers_photographer_cities'))

        # Removing M2M table for field clients on 'Photographer'
        db.delete_table(db.shorten_name(u'photographers_photographer_clients'))

        # Removing M2M table for field skills on 'Photographer'
        db.delete_table(db.shorten_name(u'photographers_photographer_skills'))


    models = {
        u'accounts.useraccount': {
            'Meta': {'object_name': 'UserAccount'},
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'my_profile'", 'unique': 'True', 'to': u"orm['auth.User']"})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'photographers.listphotographerclients': {
            'Meta': {'object_name': 'ListPhotographerClients'},
            'client': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'photographers.listphotographerskills': {
            'Meta': {'object_name': 'ListPhotographerSkills'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'skill': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'photographers.photographer': {
            'Meta': {'object_name': 'Photographer'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '3', 'to': u"orm['categories.Category']"}),
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.City']", 'symmetrical': 'False'}),
            'clients': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photographers.ListPhotographerClients']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'featured_in_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_profile': ('django.db.models.fields.URLField', [], {'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.UserAccount']", 'unique': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'personal_website': ('django.db.models.fields.URLField', [], {'max_length': '40', 'blank': 'True'}),
            'picture_portfolio': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'skills': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['photographers.ListPhotographerSkills']", 'symmetrical': 'False'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'tagline': ('django.db.models.fields.TextField', [], {}),
            'twitter_profile': ('django.db.models.fields.URLField', [], {'max_length': '40', 'blank': 'True'})
        }
    }

    complete_apps = ['photographers']