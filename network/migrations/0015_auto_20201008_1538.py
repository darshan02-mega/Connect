

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0014_auto_20200918_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_pic',
            field=models.ImageField(upload_to='profile_pic/'),
        ),
    ]
