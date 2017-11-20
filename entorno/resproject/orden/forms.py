from django import forms
from django.forms import ModelForm
from orden.models import orden,producto
from datetime import datetime


class OrdenForms(forms.ModelForm):

        pagosop=( ('efectivo','efectivo'),
                ('tarjeta de credito','tarjeta de credito'),
                ('tarjeta de debito','tarjeta de debito')

        )
        estadosop=(('en espera de pedido','en espera de pedido'),('sin pagar','sin pagar'))
        mesasop=(
                ('1','1'),
                ('2','2'),
                ('3','3'),
                ('4','4'),
                ('5','5'),
                ('6','6'),
                ('7','7'),
        )
        mesa = forms.ChoiceField(choices=mesasop, required=True)
        telefono = forms.IntegerField(required=True)
        direccion =forms.DateField()
        fecha = forms.DateField()
        producto_id = forms.SelectMultiple()
        payment_option = forms.TypedChoiceField(required=True, choices=pagosop)
        estado_orden = forms.TypedChoiceField(required=True, choices=estadosop)
        class Meta:
            model=orden
            fields  =   [
                    'mesa',
                    'telefono',
                    'direccion',
                    'fecha',
                    'producto_id',
                    'payment_option',
                    'estado_orden',
            ]
