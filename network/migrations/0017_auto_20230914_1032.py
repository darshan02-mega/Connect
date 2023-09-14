

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0016_auto_20201008_1545'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='first_name',
            field=models.CharField(blank=True, max_length=150, verbose_name='first name'),
        ),
    ]
