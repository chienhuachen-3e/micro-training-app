# Generated by Django 5.1.6 on 2025-03-05 13:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_program_created_by_enrollment_program_enrolled_users_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='created_by',
        ),
        migrations.AlterUniqueTogether(
            name='quizresponse',
            unique_together={('quiz', 'user')},
        ),
        migrations.AddField(
            model_name='quiz',
            name='points',
            field=models.PositiveIntegerField(default=10, help_text='Maximum points for this question'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='grading_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='grading_status',
            field=models.CharField(choices=[('PENDING', 'Pending Review'), ('GRADED', 'Graded')], default='PENDING', max_length=8),
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='points_earned',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='quizresponse',
            name='text_response',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='selected_choice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.quizchoice'),
        ),
        migrations.AlterField(
            model_name='quizresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='quizchoice',
            unique_together={('quiz', 'choice_text')},
        ),
        migrations.RemoveField(
            model_name='quizresponse',
            name='answer',
        ),
        migrations.RemoveField(
            model_name='quizresponse',
            name='score',
        ),
    ]
