# Generated by Django 4.0.1 on 2022-01-19 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('tanks', 'tanks'), ('healers', 'healers'), ('damage dealers', 'damage dealers'), ('merchants', 'merchants'), ('guild masters', 'guild masters'), ('questgivers', 'questgivers'), ('blacksmiths', 'blacksmiths'), ('leatherworkers', 'leatherworkers'), ('potions makers', 'potions makers'), ('spell masters', 'spell masters')], default='tanks', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
