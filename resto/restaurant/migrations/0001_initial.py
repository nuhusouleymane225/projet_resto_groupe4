# Generated by Django 2.2.3 on 2019-10-09 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('Price', models.DecimalField(decimal_places=2, max_digits=20)),
            ],
        ),
    ]
