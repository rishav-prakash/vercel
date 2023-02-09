# Generated by Django 4.1.5 on 2023-01-24 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='alert',
            fields=[
                ('Alert_id', models.AutoField(primary_key=True, serialize=False)),
                ('Title', models.CharField(default='TBA', max_length=50)),
                ('Posts', models.IntegerField(default=100)),
                ('Type', models.CharField(default='vacancy', max_length=40)),
                ('Department', models.CharField(default='Other', max_length=50)),
                ('State', models.CharField(default='Other', max_length=25)),
                ('Group', models.CharField(default='O', max_length=1)),
                ('date_of_issue', models.DateField(default='datetime.auto_now')),
                ('last_date', models.DateField(default='TBA')),
                ('url', models.URLField(default='www.google.com')),
                ('rf_gen', models.IntegerField(default=0)),
                ('rf_obc', models.IntegerField(default=0)),
                ('rf_scnst', models.IntegerField(default=0)),
                ('important', models.BooleanField(default=1)),
                ('salary', models.CharField(default='TBA', max_length=7)),
                ('qualification', models.CharField(default='Intermediate', max_length=40)),
                ('imgcode', models.CharField(default='none', max_length=8)),
            ],
        ),
    ]