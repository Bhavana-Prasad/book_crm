# Generated by Django 4.2.6 on 2023-11-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0006_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mobiles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('price', models.PositiveIntegerField()),
            ],
        ),
    ]
