# Generated by Django 4.1.2 on 2022-11-03 13:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app901', '0005_project_tag_project_vote_ratio_project_vote_total'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='tag',
            new_name='tags',
        ),
    ]
