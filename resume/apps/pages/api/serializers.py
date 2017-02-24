from rest_framework import serializers

from apps.pages.models import Page


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        read_only_fields = ('title', 'content')
        lookup_field = 'slug'
