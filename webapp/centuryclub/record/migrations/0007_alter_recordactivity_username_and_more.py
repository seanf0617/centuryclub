# Generated by Django 4.0.4 on 2022-06-07 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('record', '0006_alter_recordactivity_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordactivity',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='recordmonthtarget',
            name='username',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
