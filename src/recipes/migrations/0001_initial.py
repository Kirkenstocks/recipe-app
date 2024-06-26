# Generated by Django 4.2.11 on 2024-04-26 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('ingredients', models.CharField(max_length=300)),
                ('cooking_time', models.PositiveSmallIntegerField(help_text='in minutes')),
                ('directions', models.TextField(default='no directions')),
                ('image', models.ImageField(default='no_image.svg', upload_to='recipes')),
            ],
        ),
    ]
