# Generated by Django 4.0.5 on 2022-06-09 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mess_api', '0004_rename_conversations_list_user_conversations'),
    ]

    operations = [
        migrations.AddField(
            model_name='conversation',
            name='conversation_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]