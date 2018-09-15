# Generated by Django 2.0.3 on 2018-03-23 01:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0002_auto_20180323_0628'),
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='votes',
            name='vid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Registration.Candidate'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='votes',
            name='vote',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
