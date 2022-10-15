# Generated by Django 4.1.2 on 2022-10-15 05:31

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0005_alter_complaint_reported_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='complaint',
            name='id',
            field=models.BigAutoField(auto_created=True, default=builtins.id, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='complaint',
            name='reported_by',
            field=models.CharField(default='username', max_length=20, unique=True),
        ),
    ]
