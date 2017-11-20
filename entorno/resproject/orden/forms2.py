from django import forms

from orden.models import orden

class OrdenForms(forms.ModelForm):
    class Meta:
        pagosop=( ('efectivo','efectivo'),
                ('tarjeta de credito','tarjeta de credito'),
                ('tarjeta de debito','tarjeta de debito')

        )
        estadosop=(('en espera','en espera'))
        mesasop=(
                ('1','1'),
                ('2','2'),
                ('3','3'),
                ('4','4'),
                ('5','5'),
                ('6','6'),
                ('7','7'),
        )

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
        labels={
        'mesa:Mesa',
        'telefono:Telefono',
        'direccion:Direccion',
        'fecha:Fecha',
        'producto_id:Producto_id',
        'payment_option:Payment_option',
        'estado_orden:Estado_orden',
        }
        widgets={
        'mesa': forms.TextInput(),
        'telefono': forms.TextInput(),
        'direccion': forms.TextInput(),
        'fecha': forms.DateInput(),
        'producto_id': forms.SelectMultiple(),
        'payment_option': forms.TextInput(),
        'estado_orden': forms.TextInput(),
        }
