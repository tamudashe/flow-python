# Generated by Django 3.0.3 on 2020-02-21 20:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('networking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='industry',
            field=models.CharField(choices=[('Technology', 'tech'), ('Business', 'biz'), ('General', 'gen')], default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
    ]
