# Generated by Django 4.1.3 on 2023-07-19 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('viewed', models.BooleanField(default=False)),
                ('encrypted_message', models.BinaryField()),
            ],
        ),
    ]
