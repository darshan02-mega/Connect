

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0008_auto_20200828_1840'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follower',
            old_name='follower',
            new_name='followers',
        ),
    ]
