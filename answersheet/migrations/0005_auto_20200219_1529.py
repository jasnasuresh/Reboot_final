# Generated by Django 3.0.3 on 2020-02-19 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answersheet', '0004_answerkey_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='answersheet',
            name='key',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='answersheet.AnswerKey'),
        ),
        migrations.AlterField(
            model_name='answerkey',
            name='text',
            field=models.TextField(blank=True, null=True),
        ),
    ]
