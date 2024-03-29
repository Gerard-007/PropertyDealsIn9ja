# Generated by Django 4.1.2 on 2023-11-16 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('currency', models.CharField(blank=True, default='NGN', max_length=200, null=True, verbose_name='currency')),
                ('balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=100, verbose_name='balance')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='wallet', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='WalletTransaction',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('transaction_id', models.CharField(max_length=100, verbose_name='transaction')),
                ('currency', models.CharField(blank=True, choices=[('NGN', 'NGN'), ('USD', 'USD')], default='NGN', max_length=100, null=True, verbose_name='currency')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100, verbose_name='amount')),
                ('payment_status', models.CharField(choices=[('successful', 'successful'), ('pending', 'pending'), ('failed', 'failed')], max_length=100, verbose_name='payment status')),
                ('payment_gateway', models.CharField(default='flutterwave', max_length=100, verbose_name='payment gateway')),
                ('is_in_flow', models.BooleanField(default=False, verbose_name='concurrences')),
                ('transaction_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='wallet_transactions', to='wallets.wallet')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
