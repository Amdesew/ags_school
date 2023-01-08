# Generated by Django 4.1 on 2023-01-07 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ags_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('grade', models.FloatField()),
                ('student_id', models.FloatField()),
                ('test_one', models.TextField()),
                ('test_two', models.TextField()),
                ('mid_exam', models.TextField()),
                ('test_three', models.TextField()),
                ('final_exam', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
