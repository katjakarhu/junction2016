from django.shortcuts import render

# Create your views here.
from hapiapp.models import FakeNews
from hapiapp.serializers import FakeNewsSerializer
from rest_framework import generics

class FakeNewsList(generics.ListAPIView):
    serializer_class = FakeNewsSerializer

    def get_queryset(self):
        queryset = FakeNews.objects.all()


        #queryset = super(FakeNewsList, self).get_queryset()
        query_params = self.request.query_params
        params = query_params.keys()
        if len(params) != 1:
            return None
        
    
        query_filters = []
        custom_filters = []
        print(query_params)
        print(params)
                        
        
        
        urlparam = query_params.values()
        #
        if urlparam is not None:
            print(urlparam)
            queryset = queryset.filter(url=urlparam)

            return queryset
