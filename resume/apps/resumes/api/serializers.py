from rest_framework import serializers

from resume.apps.resumes.models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Resume
        fields = ('id', 'title', 'content', 'created_at', 'author')
