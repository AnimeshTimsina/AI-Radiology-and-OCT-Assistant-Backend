# Generated by Django 3.0.6 on 2020-05-12 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_description', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sourcecategory',
            options={'verbose_name_plural': 'Source Categories'},
        ),
        migrations.AlterModelOptions(
            name='sourcelinks',
            options={'verbose_name_plural': 'Source Links'},
        ),
    ]
