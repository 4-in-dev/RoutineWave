# Generated by Django 4.0.4 on 2022-05-23 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduletemplates', '0002_alter_scheduletemplate_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='scheduletemplate',
            name='template_name',
            field=models.CharField(default='템플릿', max_length=20, unique=True),
        ),
    ]