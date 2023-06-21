from rest_framework import serializers
from .models import Category, Brochure

class BrochureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brochure
        fields = ['title','pdf_file']


class CategorySerializer(serializers.ModelSerializer):
    # brochures = BrochureSerializer(many=True, read_only=True)
    brochures = serializers.SerializerMethodField()


    class Meta:
        model = Category
        fields = ['name', 'brochures']

    def get_brochures(self, category):
        brochures = Brochure.objects.filter(category=category)
        serializer = BrochureSerializer(brochures, many=True)
        return serializer.data
