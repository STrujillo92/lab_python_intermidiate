# Generated by Django 5.1.2 on 2024-11-04 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Arco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_arco', models.CharField(max_length=60)),
                ('resumen', models.TextField()),
                ('cap_inicial', models.IntegerField(default=0)),
                ('cap_final', models.IntegerField(default=0)),
            ],
        ),
    ]
