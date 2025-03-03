# Generated by Django 5.1.6 on 2025-02-23 08:55

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voting', '0003_election_candidate_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='election',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='voting.election'),
        ),
        migrations.AddField(
            model_name='vote',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='election',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('voter', 'election')},
        ),
    ]
