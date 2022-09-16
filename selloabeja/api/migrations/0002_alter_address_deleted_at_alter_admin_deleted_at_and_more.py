# Generated by Django 4.1.1 on 2022-09-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='beehive',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='client',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='commune',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='products',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='suscription',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='tech',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
        migrations.AlterField(
            model_name='visit',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha eliminacion'),
        ),
    ]
