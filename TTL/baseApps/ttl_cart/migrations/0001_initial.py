
# Generated by Django 2.0.7 on 2020-04-09 16:17

# Generated by Django 3.0.3 on 2020-04-09 16:02


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ttl_goods', '0001_initial'),
        ('ttl_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField(default=0, verbose_name='')),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttl_goods.GoodsInfo', verbose_name='商品')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ttl_user.UserInfo', verbose_name='用户')),
            ],
            options={
                'verbose_name': '购物车',
                'verbose_name_plural': '购物车',
            },
        ),
    ]
