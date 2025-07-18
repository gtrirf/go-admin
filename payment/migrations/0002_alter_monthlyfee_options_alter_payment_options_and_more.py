# Generated by Django 5.2.4 on 2025-07-13 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='monthlyfee',
            options={'verbose_name': "Oylik to'lov", 'verbose_name_plural': "Oylik to'lovlar"},
        ),
        migrations.AlterModelOptions(
            name='payment',
            options={'ordering': ['-paid_at']},
        ),
        migrations.AlterField(
            model_name='monthlyfee',
            name='amount',
            field=models.PositiveIntegerField(help_text='UZS da ifodalangan', verbose_name="To'lov miqdori"),
        ),
        migrations.AlterField(
            model_name='monthlyfee',
            name='description',
            field=models.TextField(blank=True, verbose_name='Tavsif'),
        ),
        migrations.AddIndex(
            model_name='monthlyfee',
            index=models.Index(fields=['amount'], name='amount_idx'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['student_id'], name='idx_payment_student'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['paid_at'], name='idx_payment_paid_at'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['valid_until'], name='idx_payment_valid_until'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['student_id', 'paid_at'], name='idx_payment_student_paid'),
        ),
        migrations.AddIndex(
            model_name='payment',
            index=models.Index(fields=['valid_until', 'paid_at'], name='idx_payment_dates'),
        ),
    ]
