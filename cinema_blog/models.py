# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Imdb(models.Model):
    poster_link = models.TextField(db_column='Poster_Link', blank=True, null=True)  # Field name made lowercase.
    series_title = models.TextField(db_column='Series_Title', blank=True, null=True)  # Field name made lowercase.
    released_year = models.IntegerField(db_column='Released_Year', blank=True, null=True)  # Field name made lowercase.
    certificate = models.TextField(db_column='Certificate', blank=True, null=True)  # Field name made lowercase.
    runtime = models.TextField(db_column='Runtime', blank=True, null=True)  # Field name made lowercase.
    genre = models.TextField(db_column='Genre', blank=True, null=True)  # Field name made lowercase.
    imdb_rating = models.IntegerField(db_column='IMDB_Rating', blank=True, null=True)  # Field name made lowercase.
    overview = models.TextField(db_column='Overview', blank=True, null=True)  # Field name made lowercase.
    meta_score = models.IntegerField(db_column='Meta_score', blank=True, null=True)  # Field name made lowercase.
    director = models.TextField(db_column='Director', blank=True, null=True)  # Field name made lowercase.
    star1 = models.TextField(db_column='Star1', blank=True, null=True)  # Field name made lowercase.
    star2 = models.TextField(db_column='Star2', blank=True, null=True)  # Field name made lowercase.
    star3 = models.TextField(db_column='Star3', blank=True, null=True)  # Field name made lowercase.
    star4 = models.TextField(db_column='Star4', blank=True, null=True)  # Field name made lowercase.
    no_of_votes = models.IntegerField(db_column='No_of_Votes', blank=True, null=True)  # Field name made lowercase.
    gross = models.TextField(db_column='Gross', blank=True, null=True)  # Field name made lowercase.

    test_field = models.TextField(db_column='test_field', blank=True, null=True)  # Field name made lowercase.


    class Meta:
        managed = True
        db_table = 'imdb'


class Authors(models.Model):
    author_name = models.TextField(db_column='author_name', blank=True, null=True)  # Field name made lowercase.
    author_email = models.TextField(db_column='author_email', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'authors'