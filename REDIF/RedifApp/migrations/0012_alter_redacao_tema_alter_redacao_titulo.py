# Generated by Django 4.0.3 on 2022-07-02 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedifApp', '0011_alter_redacao_comentario_alter_redacao_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redacao',
            name='tema',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='redacao',
            name='titulo',
            field=models.CharField(max_length=45),
        ),
    ]
