# Generated by Django 4.0.3 on 2022-07-01 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedifApp', '0006_rename_content_redacao_conteudo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redacao',
            name='conteudo',
            field=models.TextField(max_length=2000),
        ),
    ]
