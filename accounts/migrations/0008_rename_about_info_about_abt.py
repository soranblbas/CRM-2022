# Generated by Django 4.0.1 on 2022-02-02 10:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_about'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='about_info',
            new_name='abt',
        ),
    ]