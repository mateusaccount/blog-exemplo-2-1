# Generated by Django 5.1.2 on 2024-11-01 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_mensagem'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='lida',
            field=models.BooleanField(default=False),
        ),
    ]
