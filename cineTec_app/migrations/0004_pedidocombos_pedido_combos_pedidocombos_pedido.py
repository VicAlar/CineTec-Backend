# Generated by Django 4.1 on 2022-09-14 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cineTec_app', '0003_remove_pedido_combos_alter_pedidoproductos_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedidoCombos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('combo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cineTec_app.combo')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='combos',
            field=models.ManyToManyField(blank=True, through='cineTec_app.PedidoCombos', to='cineTec_app.combo'),
        ),
        migrations.AddField(
            model_name='pedidocombos',
            name='pedido',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cineTec_app.pedido'),
        ),
    ]
