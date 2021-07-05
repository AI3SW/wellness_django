# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Job(models.Model):
    session_id = models.CharField(max_length=20, blank=True, null=True)
    status = models.SmallIntegerField(blank=True, null=True)
    create_date = models.DateTimeField(blank=True, null=True)
    style_img = models.ForeignKey('StyleImg', models.DO_NOTHING, blank=True, null=True)
    input_img_id = models.IntegerField(blank=True, null=True)
    output_img_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'job'


class StyleImg(models.Model):
    file_path = models.CharField(max_length=125, blank=True, null=True)
    is_ref = models.BooleanField(blank=True, null=True)
    ref_class = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'style_img'