from rest_framework import serializers
from .models import Todo

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'task', 'completed', 'created', 'updated', 'image', 'image_url']

    def update(self, instance, validated_data):
        image = validated_data.pop('image', None)
        if image:
            instance.image = image
            instance.image_url = instance.image.url
        
        # Update other fields
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        instance.save()
        return instance



