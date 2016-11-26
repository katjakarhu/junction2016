from hapiapp.models import FakeNews
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class FakeNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeNews
        fields = ('url', 'name', 'source', 'isfake')

