# Generated by Django 4.1.7 on 2023-02-23 18:33

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
                ('title', models.CharField(max_length=1000)),
                ('owner', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
