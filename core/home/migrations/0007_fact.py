# Generated by Django 5.1.1 on 2024-09-16 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_faq'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.CharField(help_text='Name of the Material Icon (e.g., event, people).', max_length=100)),
                ('number', models.CharField(help_text="Number to display, e.g., '26', '1500+', etc.", max_length=100)),
                ('label', models.CharField(help_text="Label for the fact (e.g., 'YEARS').", max_length=100)),
            ],
        ),
    ]
