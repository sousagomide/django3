# Generated by Django 5.0 on 2023-12-14 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionariomodel',
            name='instagram',
            field=models.CharField(default='#', max_length=100, verbose_name='Instagram'),
        ),
        migrations.AddField(
            model_name='funcionariomodel',
            name='twitter',
            field=models.CharField(default='#', max_length=100, verbose_name='Twitter'),
        ),
        migrations.AlterField(
            model_name='funcionariomodel',
            name='facebook',
            field=models.CharField(default='#', max_length=100, verbose_name='Facebook'),
        ),
    ]
