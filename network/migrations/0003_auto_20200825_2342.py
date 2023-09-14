
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0002_saved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content_text',
            field=models.TextField(blank=True, max_length=140),
        ),
    ]
