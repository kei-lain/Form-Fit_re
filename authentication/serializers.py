from rest_framework import serializers

from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'

class CreatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
        # extra_kwargs = {
        #     'password': {'required': True}
        # }
    
    def validate(self, attrs):
       
        try:
            if model.objects.get(pk=user_id):
                raise serializers.ValidationError('You already have an account')
        except:
            return(attrs)
            


    def create(self, validated_data):
        person = Person.objects.create(**validated_data)
        return person

class UpdatePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('first_name','last_name','email','gender')

    def update(self, instance, validated_data):
        password = validated_data.pop('password')
        if password:
            instance.set_password(password)
        instance = super().update(instance, validated_data)
        super(UpdatePersonSerializer.self).update()
        return instance


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(style={'input_type': 'password'}, trim_whitespace=False)
    
    def validate(self, atrrs):
        email = attrs.get('email').lower()
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Please give both email and password.")

        if not Person.objects.filter(email=email).exists():
            raise serializers.ValidationError('Email does not exist.')

        user = authenticate(request=self.context.get('request'), email=email,
                            password=password)
        if not user:
            raise serializers.ValidationError("Wrong Credentials.")

        attrs['user'] = user
        return attrs
