from rest_framework import serializers
from clientes.models import Cliente
from clientes.validators import *

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validate_cpf(data['cpf']):
            raise serializers.ValidationError({'CPF':'CPF inválido'})
        
        if not validate_nome(data['nome']):
            raise serializers.ValidationError({'Nome':'Não inclua números neste campo'})
        
        if not validate_rg(data['rg']):
            raise serializers.ValidationError({'RG':'O RG deve ter 9 dígitos'})
        
        if not validate_celular(data['celular']):
            raise serializers.ValidationError({'Celular':'O número de celular deve seguir o seguinte padrão: XX XXXXX-XXXX'})

        return data
    
        