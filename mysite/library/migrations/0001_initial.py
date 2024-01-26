# Generated by Django 4.2.7 on 2023-11-21 23:40

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
                ('book_title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('cover_img', models.ImageField(upload_to='')),
                ('genre', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('pub_date', models.DateField()),
                ('isbn', models.BigIntegerField()),
                ('shelf_loc', models.SmallIntegerField()),
                ('num_available', models.SmallIntegerField()),
            ],
        ),
    ]