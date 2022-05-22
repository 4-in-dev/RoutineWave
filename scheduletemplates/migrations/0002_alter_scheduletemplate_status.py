# Generated by Django 4.0.4 on 2022-05-21 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduletemplates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scheduletemplate',
            name='status',
            field=models.CharField(choices=[('hp', '체력'), ('int', '지력'), ('will', '근성'), ('exp', '경험'), ('money', '재력'), ('ten', '행복')], default='근성', max_length=8),
        ),
    ]