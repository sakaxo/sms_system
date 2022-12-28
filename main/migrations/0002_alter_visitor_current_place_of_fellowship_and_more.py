# Generated by Django 4.1.3 on 2022-12-28 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visitor',
            name='current_place_of_fellowship',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='is_confessed_jesus',
            field=models.BooleanField(default=False, help_text='Have you Confessed Jesus Christ as your Lord and personl savior?', verbose_name='Confessed Jesus Christ?'),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='wish_to_be_a_member',
            field=models.CharField(choices=[('yes', 'Yes'), ('just visiting', 'Just Visiting'), ('still considering', 'Still considering')], max_length=30),
        ),
    ]
