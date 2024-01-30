# Generated by Django 5.0.1 on 2024-01-19 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.TextField()),
                ('sujet', models.CharField(max_length=500)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Evenement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='evenement/img/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='evenement/pdf/')),
                ('date_debut', models.DateTimeField(blank=True, null=True)),
                ('date_fin', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('sexe', models.CharField(choices=[('M', 'Masculin'), ('F', 'Féminin')], max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('profession', models.CharField(max_length=100)),
                ('pays', models.CharField(max_length=100)),
                ('situation_matrimoniale', models.CharField(choices=[('C', 'Célibataire'), ('M', 'Marié(e)'), ('D', 'Divorcé(e)'), ('V', 'Veuf/Veuve')], max_length=1)),
                ('contact', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Publicite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=200)),
                ('contenu', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='publicite/img/')),
                ('pdf', models.FileField(blank=True, null=True, upload_to='publicite/pdf/')),
                ('date_creation', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('poste', models.TextField()),
                ('photo', models.ImageField(blank=True, null=True, upload_to='team/img/')),
            ],
        ),
    ]
