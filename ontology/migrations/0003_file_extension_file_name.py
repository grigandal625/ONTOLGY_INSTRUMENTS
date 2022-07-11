# Generated by Django 4.0.6 on 2022-07-11 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology', '0002_alter_element_options_alter_file_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='extension',
            field=models.CharField(default='', max_length=255, verbose_name='Расширение'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='file',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Имя'),
            preserve_default=False,
        ),
    ]