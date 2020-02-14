# Generated by Django 3.0.3 on 2020-02-12 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoapp', '0004_auto_20200210_1544'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField(blank=True, max_length=500)),
                ('comment', models.TextField(blank=True, max_length=500)),
                ('verification', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.TextField(blank=True, max_length=500)),
                ('post', models.TextField(blank=True, max_length=500)),
                ('head', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
            ],
        ),
    ]
