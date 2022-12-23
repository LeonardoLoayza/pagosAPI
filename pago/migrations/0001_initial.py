# Generated by Django 4.1.4 on 2022-12-22 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('YT', 'Youtube'), ('SP', 'Spotify'), ('NF', 'Netflix'), ('AP', 'Amazon Video'), ('ST', 'Start+'), ('PM', 'Paramount+')], default='YT', max_length=2)),
                ('description', models.CharField(max_length=300)),
                ('logo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='PaymentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('payment_date', models.DateTimeField(auto_now_add=True)),
                ('expiration_date', models.DateTimeField()),
                ('service_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pago.services')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ExpiredPayments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penalty_fee_amount', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('payment_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pago.paymentuser')),
            ],
        ),
    ]