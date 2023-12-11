# Generated by Django 3.1.5 on 2023-12-09 19:55

import detection.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authtoken', '0003_tokenproxy'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadAlert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=detection.models.scramble_uploaded_filename, verbose_name='Uploaded image')),
                ('alert_receiver', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authtoken.token')),
            ],
        ),
    ]
