# Generated by Django 3.2.3 on 2021-06-26 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testApp', '0002_auto_20210626_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='productname',
        ),
    ]
