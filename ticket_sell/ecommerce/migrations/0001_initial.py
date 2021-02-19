# Generated by Django 3.1.6 on 2021-02-19 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Ticket name')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('code', models.CharField(max_length=20, unique=True, verbose_name='Ticket code')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecommerce.ticket')),
            ],
        ),
    ]
