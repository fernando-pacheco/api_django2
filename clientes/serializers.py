from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'CPF':'O CPF deve ter 11 dígitos'})
        
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'Nome':'Não inclua números neste campo'})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'RG':'O RG deve ter 9 dígitos'})
        
        if validate_celular(data['celular']):
            raise serializers.ValidationError({'Celular':'O celular deve ter 11 dígitos'})

        return data
    
        