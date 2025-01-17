# Generated by Django 5.1.3 on 2025-01-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=7)),
                ('address', models.CharField(blank=True, max_length=200)),
                ('city', models.CharField(blank=True, max_length=60)),
                ('state', models.CharField(blank=True, max_length=60)),
                ('country', models.CharField(blank=True, max_length=60)),
                ('document_type', models.CharField(blank=True, choices=[('NIN', 'NIN'), ("Voter's Card", "Voter's Card"), ('Passport', 'Passport')], max_length=20)),
                ('front_cover', models.ImageField(blank=True, upload_to='document_front_cover')),
                ('back_cover', models.ImageField(blank=True, upload_to='document_back_cover')),
            ],
        ),
    ]
