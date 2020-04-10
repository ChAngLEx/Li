# Generated by Django 2.2.11 on 2020-04-08 03:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Event',
                'db_table': 'df_event',
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_name', models.CharField(max_length=30, verbose_name='groupname')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Group',
                'db_table': 'df_group',
            },
        ),
        migrations.CreateModel(
            name='MovieList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Movielist',
                'verbose_name_plural': 'Movielist',
                'db_table': 'df_movielist',
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.DateTimeField(auto_now_add=True)),
                ('close_time', models.DateTimeField(auto_now=True)),
                ('vote_event', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.Event')),
                ('vote_movie', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.MovieList')),
            ],
            options={
                'verbose_name': 'Vote',
                'verbose_name_plural': 'Vote',
                'db_table': 'df_vote',
            },
        ),
        migrations.CreateModel(
            name='VoteRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote_record', models.SmallIntegerField(choices=[(1, 'Yes'), (0, 'No')], default=1)),
                ('vote', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.Vote')),
            ],
            options={
                'verbose_name': 'VoteRecord',
                'verbose_name_plural': 'VoteRecord',
                'db_table': 'df_voterecord',
            },
        ),
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='group.Group')),
            ],
            options={
                'verbose_name': 'UserGroup',
                'verbose_name_plural': 'UserGroup',
                'db_table': 'df_usergroup',
            },
        ),
    ]
