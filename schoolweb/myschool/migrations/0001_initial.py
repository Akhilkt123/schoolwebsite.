# Generated by Django 4.2.5 on 2023-09-29 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dob', models.DateField()),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('email_id', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('department', models.CharField(max_length=50)),
                ('course', models.CharField(max_length=50)),
                ('purpose', models.CharField(max_length=20)),
                ('materials_provide', models.CharField(max_length=20)),
            ],
        ),
    ]