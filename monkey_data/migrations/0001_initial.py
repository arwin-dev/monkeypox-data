# Generated by Django 4.1 on 2022-09-15 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monkey',
            fields=[
                ('ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('Status', models.CharField(blank=True, max_length=50)),
                ('Location', models.CharField(blank=True, max_length=50)),
                ('City', models.CharField(blank=True, max_length=100)),
                ('Country', models.CharField(max_length=100)),
                ('Age', models.CharField(blank=True, max_length=10, null=True)),
                ('Gender', models.CharField(blank=True, max_length=100)),
                ('Date_onset', models.CharField(blank=True, max_length=10, null=True)),
                ('Date_confirmation', models.CharField(blank=True, max_length=10)),
                ('Symptoms', models.CharField(blank=True, max_length=200, null=True)),
                ('Hospitalised', models.BooleanField(blank=True, null=True)),
                ('Date_hospitalisation', models.CharField(blank=True, max_length=10)),
                ('Isolated', models.BooleanField(blank=True, null=True)),
                ('Date_Isolation', models.CharField(blank=True, max_length=10)),
                ('Outcome', models.CharField(blank=True, max_length=200, null=True)),
                ('Date_death', models.CharField(blank=True, max_length=10)),
                ('Contact_comment', models.CharField(blank=True, max_length=100, null=True)),
                ('Contact_ID', models.CharField(blank=True, max_length=100)),
                ('Contact_location', models.CharField(blank=True, max_length=100)),
                ('Travel_history', models.BooleanField(blank=True, null=True)),
                ('Travel_history_entry', models.CharField(blank=True, max_length=100)),
                ('Travel_history_start', models.CharField(blank=True, max_length=100)),
                ('Travel_history_location', models.CharField(blank=True, max_length=100)),
                ('Travel_history_country', models.CharField(blank=True, max_length=100)),
                ('Genomics_Metadata', models.CharField(blank=True, max_length=100)),
                ('Confirmation_method', models.CharField(blank=True, max_length=100)),
                ('Source', models.CharField(blank=True, max_length=300)),
                ('Source_II', models.CharField(blank=True, max_length=300)),
                ('Date_entry', models.CharField(blank=True, max_length=10)),
                ('Date_last_modified', models.CharField(blank=True, max_length=10)),
                ('Source_III', models.CharField(blank=True, max_length=300)),
                ('Source_IV', models.CharField(blank=True, max_length=300)),
                ('Country_ISO3', models.CharField(max_length=50)),
            ],
        ),
    ]
