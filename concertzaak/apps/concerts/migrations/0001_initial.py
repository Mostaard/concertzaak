# Generated by Django 3.2.8 on 2021-10-05 19:43

from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailimages', '0023_add_choose_permissions'),
        ('wagtailcore', '0062_comment_models_and_pagesubscription'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConcertsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('no_concerts', models.CharField(default='', help_text='Bericht wanneer er geen concerten ingepland zijn', max_length=150)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ConcertPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('concert_date', models.DateField()),
                ('introduction', models.CharField(blank=True, max_length=150)),
                ('information', wagtail.fields.RichTextField()),
                ('facebook_link', models.URLField()),
                ('ticket_link', models.URLField()),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='wagtailimages.image')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='concerts.location')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
