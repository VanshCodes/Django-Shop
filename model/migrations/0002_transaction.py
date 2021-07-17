# Generated by Django 3.2.5 on 2021-07-17 12:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('transactionID', models.AutoField(primary_key=True, serialize=False)),
                ('price', models.IntegerField()),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('paid', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='model.customer')),
            ],
        ),
    ]