# Generated by Django 3.2.1 on 2021-07-15 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=50)),
                ('letter', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='CV',
        ),
    ]
