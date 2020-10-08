# Generated by Django 2.1.5 on 2020-10-07 06:57

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
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_issue', models.DateField()),
                ('actual_return_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='LoanSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('loansubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.LoanSubject')),
                ('isbn', models.CharField(max_length=13)),
                ('subject', models.CharField(max_length=50)),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='LibraryManagement.Author')),
            ],
            bases=('LibraryManagement.loansubject',),
        ),
        migrations.CreateModel(
            name='Container',
            fields=[
                ('loansubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.LoanSubject')),
            ],
            bases=('LibraryManagement.loansubject',),
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('loansubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.LoanSubject')),
                ('device_type', models.CharField(max_length=50)),
            ],
            bases=('LibraryManagement.loansubject',),
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('loansubject_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.LoanSubject')),
            ],
            bases=('LibraryManagement.loansubject',),
        ),
        migrations.CreateModel(
            name='PermLoan',
            fields=[
                ('loan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.Loan')),
            ],
            bases=('LibraryManagement.loan',),
        ),
        migrations.CreateModel(
            name='TempLoan',
            fields=[
                ('loan_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='LibraryManagement.Loan')),
                ('expected_return_date', models.DateField()),
            ],
            bases=('LibraryManagement.loan',),
        ),
        migrations.AddField(
            model_name='loansubject',
            name='loan_object',
            field=models.ManyToManyField(to='LibraryManagement.Loan'),
        ),
        migrations.AddField(
            model_name='loan',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]