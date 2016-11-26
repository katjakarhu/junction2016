from django.shortcuts import render

# Create your views here.
from hapiapp.models import FakeNews
from hapiapp.serializers import FakeNewsSerializer
from rest_framework import generics
from rest_framework.response import Response

class FakeNewsList(generics.ListAPIView):
    queryset = FakeNews.objects.all()

    # print(queryset)
    
    serializer_class = FakeNewsSerializer

 
    def list(self, request, *args, **kwargs):
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1:
            return None
        
    
        query_filters = []
        custom_filters = []
        #print(query_dict)
        #print(query_keys)
                        
        
        
        urlParamList = query_dict.getlist("url")
        #
        jsonDicts = {}
        i = 0
        for urlParam in urlParamList:
            jsonDicts[i] = {}
            jsonDicts[i]['url'] = urlParam
            if i%2 == 0:
                source = "Very Respectable Authority Says So"
                sourceUrl = "http://www.google.com/"
                foo = "true"
            else:
                foo = "false"
                source = "Underpants Gnomes LLC"
                sourceUrl = "http://www.google.com/"
            jsonDicts[i]['isFake'] = foo
            jsonDicts[i]['source'] = source
            i = i + 1
            
        

        
        return Response(jsonDicts)
