# Generated by Django 4.1.1 on 2023-04-03 19:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booktype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('btype', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(default=models.CharField(max_length=100, unique=True))),
            ],
            options={
                'ordering': ('btype',),
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(max_length=150)),
                ('slug', models.SlugField(default=models.CharField(max_length=150))),
                ('author_name', models.CharField(max_length=150)),
                ('price', models.FloatField()),
                ('image', models.ImageField(blank=True, default=' ', null=True, upload_to='media/uploads/')),
                ('thumbnail', models.ImageField(blank=True, default=' ', null=True, upload_to='media/uploads/')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='type', to='book.booktype')),
            ],
            options={
                'ordering': ('book_name',),
            },
        ),
    ]
