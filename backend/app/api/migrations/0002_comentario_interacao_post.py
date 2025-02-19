# Generated by Django 5.1.2 on 2024-12-15 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('conteudo', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField()),
            ],
            options={
                'db_table': 'comentario',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Interacao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('data_interacao', models.DateTimeField()),
            ],
            options={
                'db_table': 'interacao',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('conteudo', models.CharField(max_length=255)),
                ('data_criacao', models.DateTimeField()),
                ('midia', models.TextField()),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
    ]
