# Generated by Django 3.0.8 on 2020-07-08 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('adress', models.CharField(max_length=20)),
                ('ph', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
