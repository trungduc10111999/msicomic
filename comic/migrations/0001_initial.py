# Generated by Django 3.0.2 on 2020-01-04 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000)),
                ('types', models.CharField(max_length=100)),
                ('excerpt', models.TextField(max_length=200)),
                ('description', models.TextField()),
                ('picture', models.ImageField(upload_to='comic_picture')),
            ],
        ),
    ]
