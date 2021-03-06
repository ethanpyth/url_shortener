# Generated by Django 4.0.3 on 2022-03-27 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiniURL', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniurl',
            name='date_creation',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement"),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='long_url',
            field=models.URLField(unique=True, verbose_name='URL à réduire'),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='nbre_access',
            field=models.IntegerField(default=0, verbose_name="Nombre d'accès à l'url"),
        ),
        migrations.AlterField(
            model_name='miniurl',
            name='pseudo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
