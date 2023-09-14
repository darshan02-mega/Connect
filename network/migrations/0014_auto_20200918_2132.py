

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0013_auto_20200902_1701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(default='no_pic.png', upload_to='profile_pic/'),
        ),
    ]
