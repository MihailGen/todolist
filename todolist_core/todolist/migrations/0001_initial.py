# Generated by Django 5.1.2 on 2024-10-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Тема задачи')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('due_date', models.DateTimeField(blank=True, null=True, verbose_name='Cроки выполнения')),
                ('tags', models.TextField(default='задачи', verbose_name='Теги')),
                ('author', models.CharField(blank=True, max_length=50, null=True, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'задача',
                'verbose_name_plural': 'задачи',
            },
        ),
    ]
