# Generated by Django 4.0.4 on 2022-05-29 21:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Type your name', max_length=200)),
                ('email', models.EmailField(help_text='Type your Email', max_length=75)),
                ('phone', models.CharField(help_text='Type your phone number start with 05', max_length=10)),
                ('date_created', models.DateTimeField(auto_now_add=True, help_text='Date created')),
                ('profile', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(help_text='Type name of the item', max_length=100)),
                ('brand', models.CharField(help_text='Type the brand name', max_length=100)),
                ('description', models.TextField(blank=True)),
                ('price', models.IntegerField(help_text='Type price of the product')),
                ('photo', models.ImageField(upload_to='product/photo/')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='interface.seller')),
            ],
        ),
    ]
