# Generated by Django 4.2.4 on 2023-08-31 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.CharField(max_length=255)),
                ('pub_date', models.DateField(default='', null=True)),
                ('auther', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
