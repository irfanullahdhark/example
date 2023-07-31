from rest_framework import serializers
from .models import Student


def name_start_with_i(value):
    if value[0] != 'i':
        raise serializers.ValidationError('name must start with i')


class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100,validators=[name_start_with_i,])
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.roll = validated_data.get('roll', instance.roll)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance

    # def validate_roll(self,value):
    #     if value > 200:
    #         raise serializers.ValidationError('roll no must be less then 200')
    #     return value


    # def validate(self, attrs):
    #     nm = attrs.get('name')
    #     rl = attrs.get('roll')
    #     ct = attrs.get('city')
    #
    #     if ct != 'kabul' or nm.lower() == 'kamran':
    #         raise serializers.ValidationError('city must be kabul name will not be kamran')
    #     return attrs
