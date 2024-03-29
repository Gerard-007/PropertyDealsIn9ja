# Generated by Django 4.1.2 on 2023-11-16 18:07

import apps.properties.models
import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('agents', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=120, null=True)),
                ('slug', autoslug.fields.AutoSlugField(always_update=True, editable=False, populate_from='name', unique_with=('uploaded_at',))),
                ('description', models.TextField(blank=True, help_text='Tell us more about this property...', null=True)),
                ('property_image', models.ImageField(blank=True, help_text='Main View', null=True, upload_to=apps.properties.models.upload_dir)),
                ('exterior_image1', models.ImageField(blank=True, help_text='Exterior View1', null=True, upload_to=apps.properties.models.upload_dir)),
                ('exterior_image2', models.ImageField(blank=True, help_text='Exterior View2', null=True, upload_to=apps.properties.models.upload_dir)),
                ('interior_image1', models.ImageField(blank=True, help_text='Interior View1', null=True, upload_to=apps.properties.models.upload_dir)),
                ('interior_image2', models.ImageField(blank=True, help_text='Interior View2', null=True, upload_to=apps.properties.models.upload_dir)),
                ('price', models.DecimalField(decimal_places=2, default=0.0, help_text='0.00', max_digits=10)),
                ('payment_plan', models.CharField(blank=True, choices=[('Mthly', 'Monthly'), ('Qtly', 'Quarterly'), ('1/2Yr', 'Half Yearly'), ('Yr', 'Annually'), ('None', 'None')], default='None', max_length=144, null=True)),
                ('tax', models.DecimalField(blank=True, decimal_places=2, default=0.15, help_text="Property Tax '10% property tax charged'", max_digits=6, null=True)),
                ('featured', models.BooleanField(default=False)),
                ('views_count', models.IntegerField(default=0)),
                ('like_count', models.BigIntegerField(default=0)),
                ('property_type', models.CharField(blank=True, choices=[('Apartment', 'Apartment'), ('BQ', 'Bq'), ('Terrace', 'Terrace'), ('Semi Detached', 'Semi Detached'), ('Fully Detached', 'Fully Detached'), ('Office', 'Office'), ('Warehouse', 'Warehouse'), ('Commercial', 'Commercial'), ('Land', 'Land'), ('Other', 'Other')], default='Property Type', max_length=144, null=True)),
                ('property_status', models.CharField(blank=True, choices=[('For Rent', 'For Rent'), ('For Sale', 'For Sale'), ('Auction', 'Auction'), ('Lease', 'Lease'), ('Short Let', 'Short Let')], default='Property Status', max_length=144, null=True)),
                ('plot_area', models.IntegerField(blank=True, help_text='The plot/size measured in Sqft...', null=True)),
                ('no_bed_room', models.IntegerField(blank=True, default=0, help_text='Number of bedroom exception of land', null=True)),
                ('no_bath_room', models.IntegerField(blank=True, default=0, help_text='Number of bathroom  exception of land', null=True)),
                ('state', models.CharField(blank=True, help_text='State', max_length=144, null=True)),
                ('city', models.CharField(blank=True, help_text='City/LGA', max_length=144, null=True)),
                ('local_area', models.CharField(blank=True, help_text='Nearest Bustop/Local Area', max_length=144, null=True)),
                ('street_address', models.CharField(blank=True, help_text='Street Address/House Number', max_length=144, null=True)),
                ('uploaded_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='like', to=settings.AUTH_USER_MODEL)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='agents.agent')),
            ],
            options={
                'verbose_name_plural': 'Properties',
                'ordering': ('-uploaded_at',),
                'unique_together': {('name', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='PropertyMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_image', models.ImageField(blank=True, help_text='Upload images', null=True, upload_to=apps.properties.models.property_media_upload_dir)),
                ('img_property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_images', to='properties.property')),
                ('uploaded_by', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='my_property_images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to=settings.AUTH_USER_MODEL)),
                ('property', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_comment', to='properties.property')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
