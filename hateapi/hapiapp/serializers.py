from hapiapp.models import FakeNews, FakeSite
from rest_framework import routers, serializers, viewsets

# Serializers define the API representation.
class FakeNewsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeNews
        fields = ('url', 'name', 'source', 'isfake')

class FakeSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FakeSite
        fields = ('site')

