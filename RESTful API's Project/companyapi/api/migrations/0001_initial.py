# Generated by Django 3.2 on 2023-07-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('about', models.TextField()),
                ('type', models.CharField(choices=[('IT', 'IT'), ('Non-IT', 'Non-IT'), ('Mobile Phones', 'Mobile Phones')], max_length=100)),
                ('added_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
