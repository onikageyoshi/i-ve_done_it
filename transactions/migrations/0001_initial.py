# Generated by Django 5.1.3 on 2025-01-10 20:26

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loan_transfer',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('SUCCESSFUL', 'SUCCESSFUL'), ('FAILED', 'FAILED'), ('PENDING', 'PENDING')], max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('source_account_number', models.CharField(max_length=11)),
                ('destination_account_number', models.CharField(max_length=11)),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Loan_withdrawal',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('status', models.CharField(choices=[('SUCCESSFUL', 'SUCCESSFUL'), ('FAILED', 'FAILED'), ('PENDING', 'PENDING')], max_length=15)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('account_number', models.CharField(max_length=11)),
                ('transaction_type', models.CharField(choices=[('WITHDRAWAL', 'WITHDRAWAL'), ('REPAYMENT', 'REPAYMENT')], max_length=30)),
            ],
            options={
                'ordering': ['-timestamp'],
                'abstract': False,
            },
        ),
    ]
