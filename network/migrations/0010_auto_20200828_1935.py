

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0009_auto_20200828_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
