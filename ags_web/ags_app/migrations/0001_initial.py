# Generated by Django 4.1 on 2023-01-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('grade', models.FloatField()),
                ('student_id', models.FloatField()),
                ('test_one', models.CharField(max_length=200)),
                ('test_two', models.CharField(max_length=200)),
                ('mid_exam', models.CharField(max_length=200)),
                ('test_three', models.CharField(max_length=200)),
                ('final_exam', models.CharField(max_length=200)),
            ],
        ),
    ]