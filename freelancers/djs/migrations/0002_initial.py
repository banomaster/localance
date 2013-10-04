# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ListDJGenres'
        db.create_table(u'djs_listdjgenres', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('genre', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'djs', ['ListDJGenres'])

        # Adding model 'ListDJOccasions'
        db.create_table(u'djs_listdjoccasions', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('occasion', self.gf('django.db.models.fields.CharField')(max_length=30)),
        ))
        db.send_create_signal(u'djs', ['ListDJOccasions'])

        # Adding model 'DJ'
        db.create_table(u'djs_dj', (
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
            ('soundcloud_profile', self.gf('django.db.models.fields.URLField')(max_length=50)),
            ('picture_portfolio', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal(u'djs', ['DJ'])

        # Adding M2M table for field cities on 'DJ'
        m2m_table_name = db.shorten_name(u'djs_dj_cities')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dj', models.ForeignKey(orm[u'djs.dj'], null=False)),
            ('city', models.ForeignKey(orm[u'cities.city'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dj_id', 'city_id'])

        # Adding M2M table for field occasions on 'DJ'
        m2m_table_name = db.shorten_name(u'djs_dj_occasions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dj', models.ForeignKey(orm[u'djs.dj'], null=False)),
            ('listdjoccasions', models.ForeignKey(orm[u'djs.listdjoccasions'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dj_id', 'listdjoccasions_id'])

        # Adding M2M table for field genres on 'DJ'
        m2m_table_name = db.shorten_name(u'djs_dj_genres')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('dj', models.ForeignKey(orm[u'djs.dj'], null=False)),
            ('listdjgenres', models.ForeignKey(orm[u'djs.listdjgenres'], null=False))
        ))
        db.create_unique(m2m_table_name, ['dj_id', 'listdjgenres_id'])


    def backwards(self, orm):
        # Deleting model 'ListDJGenres'
        db.delete_table(u'djs_listdjgenres')

        # Deleting model 'ListDJOccasions'
        db.delete_table(u'djs_listdjoccasions')

        # Deleting model 'DJ'
        db.delete_table(u'djs_dj')

        # Removing M2M table for field cities on 'DJ'
        db.delete_table(db.shorten_name(u'djs_dj_cities'))

        # Removing M2M table for field occasions on 'DJ'
        db.delete_table(db.shorten_name(u'djs_dj_occasions'))

        # Removing M2M table for field genres on 'DJ'
        db.delete_table(db.shorten_name(u'djs_dj_genres'))


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
        u'djs.dj': {
            'Meta': {'object_name': 'DJ'},
            'about': ('django.db.models.fields.TextField', [], {}),
            'available': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'default': '3', 'to': u"orm['categories.Category']"}),
            'cities': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['cities.City']", 'symmetrical': 'False'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'featured_in_category': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'genres': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['djs.ListDJGenres']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'linkedin_profile': ('django.db.models.fields.URLField', [], {'max_length': '50', 'blank': 'True'}),
            'modified': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['accounts.UserAccount']", 'unique': 'True'}),
            'nickname': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'occasions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['djs.ListDJOccasions']", 'symmetrical': 'False'}),
            'personal_website': ('django.db.models.fields.URLField', [], {'max_length': '40', 'blank': 'True'}),
            'picture_portfolio': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'default': "''", 'max_length': '255', 'blank': 'True'}),
            'soundcloud_profile': ('django.db.models.fields.URLField', [], {'max_length': '50'}),
            'tagline': ('django.db.models.fields.TextField', [], {}),
            'twitter_profile': ('django.db.models.fields.URLField', [], {'max_length': '40', 'blank': 'True'})
        },
        u'djs.listdjgenres': {
            'Meta': {'object_name': 'ListDJGenres'},
            'genre': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'djs.listdjoccasions': {
            'Meta': {'object_name': 'ListDJOccasions'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'occasion': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['djs']