# Generated by Django 4.1 on 2022-09-30 03:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("identifier", "0005_utilisateur_has_module_perms"),
    ]

    operations = [
        migrations.RemoveField(model_name="utilisateur", name="has_module_perms",),
    ]