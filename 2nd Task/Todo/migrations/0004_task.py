# Generated by Django 4.2.7 on 2023-11-27 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0003_alter_user1_options_alter_user1_managers_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=200)),
                ('task_status', models.CharField(choices=[('incomplete', 'Incomplete'), ('delayed', 'Delayed'), ('in-progress', 'In Progress'), ('closed', 'Closed')], max_length=20)),
            ],
        ),
    ]
