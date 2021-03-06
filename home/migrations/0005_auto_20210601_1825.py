# Generated by Django 3.2.3 on 2021-06-01 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_customer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='first_name',
            new_name='fname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='last_name',
            new_name='lname',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='password',
            new_name='pass1',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='phone',
        ),
        migrations.AddField(
            model_name='customer',
            name='pass2',
            field=models.CharField(default='', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='username',
            field=models.CharField(default='...', max_length=12),
        ),
    ]
