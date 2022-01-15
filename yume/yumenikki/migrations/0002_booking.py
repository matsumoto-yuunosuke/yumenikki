# Generated by Django 3.0.2 on 2022-01-15 15:52

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yumenikki', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nick_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='ニックネーム')),
                ('place', models.TextField(default='', verbose_name='招待url')),
                ('start', models.DateTimeField(default=django.utils.timezone.now, verbose_name='開始時間')),
                ('end', models.DateTimeField(default=django.utils.timezone.now, verbose_name='終了時間')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='yumenikki.DreamModel', verbose_name='テスト夢')),
            ],
        ),
    ]
