# Generated by Django 3.2.7 on 2021-10-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('critique', '0002_rename_dev_develop'),
    ]

    operations = [
        migrations.AddField(
            model_name='develop',
            name='article',
            field=models.FileField(default='static/def/check.docx', upload_to=''),
        ),
        migrations.AddField(
            model_name='develop',
            name='article_topic',
            field=models.CharField(default='none', max_length=100),
        ),
    ]
