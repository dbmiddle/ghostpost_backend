from rest_framework.serializers import HyperlinkedModelSerializer

from api.models import BoastsAndRoasts


class BoastsAndRoastsSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = BoastsAndRoasts
        fields = ('is_boast',
                  'content',
                  'votescore',
                  'upvotes',
                  'downvotes',
                  'date')
