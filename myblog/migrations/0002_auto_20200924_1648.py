# Generated by Django 3.0.5 on 2020-09-24 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=220)),
                ('author', models.CharField(max_length=15)),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]