# Generated by Django 4.2 on 2024-02-11 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('average_rating', models.FloatField()),
                ('total_ratings', models.IntegerField()),
                ('edition_number', models.IntegerField()),
                ('publish_year', models.IntegerField()),
            ],
        ),
    ]
