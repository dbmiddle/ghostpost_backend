from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from api.serializers import BoastsAndRoastsSerializer
from api.models import BoastsAndRoasts
# Create your views here.


class BoastsAndRoastsViewSet(ModelViewSet):
    serializer_class = BoastsAndRoastsSerializer
    basename = 'boastsandroasts'
    queryset = BoastsAndRoasts.objects.all()

    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        upvotecount = self.get_object()
        upvotecount.upvotes += 1
        upvotecount.save()
        return Response({'upvotecount': upvotecount.upvotes})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        downvotecount = self.get_object()
        downvotecount.downvotes += 1
        downvotecount.save()
        return Response({'downvotecount': downvotecount.downvotes})
