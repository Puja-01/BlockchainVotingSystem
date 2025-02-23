# Generated by Django 5.1.6 on 2025-02-23 09:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0004_vote_election_vote_timestamp_alter_election_name_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='election',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election'),
        ),
        migrations.AlterField(
            model_name='election',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='election',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='vote',
            name='election',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voting.election'),
        ),
    ]
