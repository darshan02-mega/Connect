

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0010_auto_20200828_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='follower',
            name='followers',
            field=models.ManyToManyField(blank=True, null=True, related_name='following', to=settings.AUTH_USER_MODEL),
        ),
    ]
