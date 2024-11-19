# Generated by Django 5.0 on 2024-10-17 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('weight', models.FloatField()),
                ('height', models.IntegerField(default=130)),
                ('sex', models.IntegerField(default=0)),
                ('age', models.IntegerField(default=18)),
                ('activePerDay', models.IntegerField(default=0)),
            ],
        ),
    ]