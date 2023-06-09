# Generated by Django 4.2.1 on 2023-05-15 11:29

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
                ('title', models.CharField(max_length=33)),
                ('price', models.DecimalField(decimal_places=2, max_digits=23)),
                ('description', models.TextField()),
                ('checkk', models.BooleanField(default=True)),
            ],
        ),
    ]
