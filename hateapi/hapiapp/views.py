from django.shortcuts import render

# Create your views here.
from hapiapp.models import FakeNews
from hapiapp.serializers import FakeNewsSerializer
from rest_framework import generics

class FakeNewsList(generics.ListAPIView):
    serializer_class = FakeNewsSerializer

    def get_queryset(self):
      

        #queryset = super(FakeNewsList, self).get_queryset()
        query_params = self.request.query_params
        params = query_params.keys()
        if len(params) != 1:
            return None
        
    
        query_filters = []
        custom_filters = []
        print(query_params)
        print(params)
                        
        
        
        #urlparam = query_filters.get("url")
        #if urlparam is not None:
        #    print("!!!!!!!!!!!!!! " + urlparam)
        #    queryset = queryset.filter(fakenews__url=urlparam)


        return queryset
