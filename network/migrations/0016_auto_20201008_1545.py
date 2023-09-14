

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0015_auto_20201008_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, max_length=160, null=True),
        ),
    ]
