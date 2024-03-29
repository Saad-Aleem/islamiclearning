# Generated by Django 3.2.7 on 2021-10-02 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_rename_critique_critic'),
    ]

    operations = [
        migrations.AddField(
            model_name='critic',
            name='critic_email',
            field=models.EmailField(default='none', max_length=254),
        ),
        migrations.AddField(
            model_name='critic',
            name='critic_question',
            field=models.FileField(default='static/def/check.docx', upload_to=''),
        ),
        migrations.AddField(
            model_name='subs',
            name='subscriber_email',
            field=models.EmailField(default='none', max_length=254),
        ),
    ]
