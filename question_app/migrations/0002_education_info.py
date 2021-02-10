# Generated by Django 2.1.7 on 2020-09-20 10:47

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('question_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='education_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('education_filled', models.IntegerField(default=0)),
                ('Education_type', models.CharField(choices=[('10th Class', '10th Class'), ('12th Class', '12th Class'), ('Graduation', 'Graduation'), ('Post Graduation', 'Post Graduation'), ('Doctorate', 'Doctorate')], max_length=20)),
                ('School_or_College_Name', models.CharField(max_length=100)),
                ('Education_Percentage', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
