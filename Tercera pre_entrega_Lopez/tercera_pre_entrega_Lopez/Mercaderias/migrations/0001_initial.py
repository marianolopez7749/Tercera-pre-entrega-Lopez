# Generated by Django 4.1.7 on 2023-04-08 15:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('desctipcion', models.CharField(max_length=40)),
                ('codigo', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Proovedores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razon_social', models.CharField(max_length=40)),
                ('titular', models.CharField(max_length=40)),
                ('Cuit', models.IntegerField(verbose_name=9)),
                ('domicilio', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(verbose_name=6)),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mercaderias.productos')),
            ],
        ),
        migrations.AddField(
            model_name='productos',
            name='Cuit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mercaderias.proovedores'),
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orden_compra', models.IntegerField()),
                ('factura_compra', models.CharField(max_length=40)),
                ('cantidad', models.IntegerField(verbose_name=4)),
                ('Cuit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mercaderias.proovedores')),
                ('codigo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Mercaderias.productos')),
            ],
        ),
    ]
