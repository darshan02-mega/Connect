

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0006_auto_20200827_0017'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='savers',
            field=models.ManyToManyField(related_name='saved', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Saved',
        ),
    ]
