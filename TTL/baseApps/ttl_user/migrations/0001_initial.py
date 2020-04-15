# Generated by Django 2.0.7 on 2020-04-15 15:39

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ttl_goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsBrowser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('browser_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='浏览时间')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttl_goods.GoodsInfo', verbose_name='商品ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=40)),
                ('email', models.EmailField(error_messages={'logo': 'Unique 不可以重复'}, max_length=254, unique=True)),
                ('shou', models.TextField(default='[]', max_length=5000)),
                ('youbian', models.CharField(default='', max_length=6)),
                ('phone', models.CharField(default='', max_length=11)),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
        migrations.AddField(
            model_name='goodsbrowser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttl_user.UserInfo', verbose_name='用户ID'),
        ),
    ]
