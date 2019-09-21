# Generated by Django 2.2.2 on 2019-09-07 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iron_store_transactions', '0008_auto_20190907_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='IronStoreDailyExpenses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('amount', models.CharField(default=0, max_length=100)),
                ('today_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]