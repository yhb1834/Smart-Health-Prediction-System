# Generated by Django 3.2.3 on 2021-05-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor_user',
            name='user_name',
            field=models.CharField(blank=True, max_length=20, verbose_name='username'),
        ),
        migrations.AlterField(
            model_name='doctor_user',
            name='user_id',
            field=models.CharField(max_length=20, verbose_name='userid'),
        ),
    ]