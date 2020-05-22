# Generated by Django 2.2.6 on 2020-04-03 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(default=0, verbose_name='分数')),
                ('score_rank', models.PositiveIntegerField(choices=[(0, '优秀'), (1, '良好'), (2, '及格'), (3, '不及格')], default=3, verbose_name='成绩等级')),
                ('start_test_time', models.DateTimeField(null=True, verbose_name='考试开始时间')),
                ('end_test_time', models.DateTimeField(null=True, verbose_name='考试结束时间')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '考试结果',
                'verbose_name_plural': '考试结果',
                'db_table': 'exam_result',
            },
        ),
        migrations.CreateModel(
            name='ExamSort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=100, verbose_name='卷子题目')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '卷子',
                'verbose_name_plural': '卷子',
                'db_table': 'exam_sort',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(default='', max_length=1024, verbose_name='问题')),
                ('standard_answer', models.CharField(default='', help_text='多个答案以逗号分隔', max_length=20, verbose_name='标准答案')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('choice_status', models.PositiveIntegerField(choices=[(0, '单选'), (1, '多选')], default=0, verbose_name='选题类型')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('title', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='exam_title', to='exam.ExamSort', verbose_name='考试题目')),
            ],
            options={
                'verbose_name': '试题库',
                'verbose_name_plural': '试题库',
                'db_table': 'questions',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='TestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(default='', max_length=20, verbose_name='答案')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('exam_result', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='result_test_record', to='exam.ExamResult', verbose_name='考试结果')),
                ('question', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='questions_record', to='exam.Questions', verbose_name='题目')),
            ],
            options={
                'verbose_name': '考试记录',
                'verbose_name_plural': '考试记录',
                'db_table': 'test_record',
            },
        ),
        migrations.CreateModel(
            name='TestOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(default='', max_length=1024, verbose_name='选项')),
                ('status', models.PositiveIntegerField(choices=[(1, '正常'), (0, '删除')], default=1, verbose_name='状态')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('question', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='question_options', to='exam.Questions', verbose_name='题目')),
            ],
            options={
                'verbose_name': '试题选项',
                'verbose_name_plural': '试题选项',
                'db_table': 'test_options',
            },
        ),
        migrations.AddField(
            model_name='examresult',
            name='title',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='title_results', to='exam.ExamSort', verbose_name='考试题目'),
        ),
        migrations.AddField(
            model_name='examresult',
            name='user',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='user_results', to=settings.AUTH_USER_MODEL, verbose_name='考生'),
        ),
    ]
