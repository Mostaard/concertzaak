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
            name='LandingPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('landing_text', wagtail.fields.RichTextField(default='', max_length=160)),
                ('rehearsal_text', wagtail.fields.RichTextField(default='', max_length=200)),
                ('concerts_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.page')),
                ('landing_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image')),
                ('rehearsal_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailimages.image')),
                ('rehearsal_page', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
