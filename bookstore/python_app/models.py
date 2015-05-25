# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models


class Book(models.Model):
    book_id = models.FloatField(primary_key=True)
    book_img = models.BinaryField(blank=True, null=True)
    book_title = models.CharField(max_length=100)
    book_price = models.FloatField()
    book_author = models.CharField(max_length=100)
    book_pages = models.FloatField()
    book_publisher = models.CharField(max_length=100)
    book_description = models.CharField(max_length=500, blank=True, null=True)
    category = models.ForeignKey('Categories', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book'


class Categories(models.Model):
    category_id = models.FloatField(primary_key=True)
    category_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class UserBought(models.Model):
    user_id = models.FloatField(primary_key=True)
    book = models.ForeignKey(Book)

    class Meta:
        managed = False
        db_table = 'user_bought'


class UserLikedCategories(models.Model):
    user_id = models.FloatField(primary_key=True)
    category = models.ForeignKey(Categories)

    class Meta:
        managed = False
        db_table = 'user_liked_categories'


class Users(models.Model):
    user_id = models.FloatField(primary_key=True)
    username = models.CharField(max_length=20)
    user_password = models.CharField(max_length=20)
    user_email = models.CharField(max_length=40, blank=True, null=True)
    user_address = models.CharField(max_length=200, blank=True, null=True)
    user_phone = models.FloatField()
    user_type = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
