# Generated by Django 4.0.6 on 2022-07-11 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ontology_model', '0002_alter_elementtype_options_alter_relationtype_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationtype',
            name='default_reflexivity',
            field=models.IntegerField(blank=True, choices=[(None, 'Не указано'), (1, 'Рефлексивная'), (2, 'Антирефлексивная')], default=None, null=True, verbose_name='Рефлексивность по умолчанию'),
        ),
        migrations.AlterField(
            model_name='relationtype',
            name='default_symmetry',
            field=models.IntegerField(blank=True, choices=[(None, 'Не указано'), (1, 'Симментричная'), (2, 'Антисиметричная')], default=None, null=True, verbose_name='Симметричность по умолчанию'),
        ),
        migrations.AlterField(
            model_name='relationtype',
            name='default_transitivity',
            field=models.IntegerField(choices=[(1, 'Транзитивная'), (2, 'Интранзитивная')], default=2, verbose_name='Транзитивность по умолчанию'),
        ),
    ]