# Generated by Django 4.0.4 on 2022-05-27 01:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('achievement', '0002_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.CharField(default='D', max_length=3)),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rank_writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
