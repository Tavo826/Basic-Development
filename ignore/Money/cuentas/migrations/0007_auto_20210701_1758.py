# Generated by Django 3.1.7 on 2021-07-01 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuentas', '0006_auto_20210630_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Categoría'),
        ),
        migrations.RemoveField(
            model_name='cuenta',
            name='categoria',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='categoria',
            field=models.ManyToManyField(related_name='get_transaction', to='cuentas.Category', verbose_name='Categoría'),
        ),
    ]