# Generated by Django 2.0.6 on 2018-06-16 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('content1', models.TextField()),
                ('content2', models.TextField()),
            ],
        ),
    ]
