# Generated by Django 3.2.7 on 2021-10-02 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='critique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('critic_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='subs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber_Name', models.CharField(max_length=50)),
            ],
        ),
    ]
