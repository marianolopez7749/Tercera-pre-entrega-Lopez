# Generated by Django 4.1.7 on 2023-04-08 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mercaderias', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Proovedores',
            new_name='Proveedores',
        ),
        migrations.RenameField(
            model_name='productos',
            old_name='desctipcion',
            new_name='descripcion',
        ),
    ]