# Generated by Django 4.2.6 on 2023-11-10 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_donate_money_hide'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donate_money',
            name='hide',
        ),
        migrations.AddField(
            model_name='donate_money',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='donate_money',
            name='email',
            field=models.EmailField(default='', max_length=254),
        ),
    ]
