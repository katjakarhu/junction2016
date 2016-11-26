from django.shortcuts import render

# Create your views here.
from hapiapp.models import FakeNews, FakeSite

from hapiapp.serializers import FakeNewsSerializer, FakeSiteSerializer
from rest_framework import generics
from rest_framework.response import Response
from urllib.parse import urlparse
        
class FakeNewsList(generics.ListAPIView):
 
    queryset = FakeSite.objects.all()


    print(queryset)
    
    serializer_class = FakeSiteSerializer
 
    def list(self, request, *args, **kwargs):
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1:
            return None
    
        query_filters = []
        custom_filters = []
        
        urlParamList = query_dict.getlist("url")

        jsonDicts = {"response":[]}
        i = 0
        for urlParam in urlParamList:
            parsed_uri = urlparse(urlParam)
            domain = '{uri.netloc}'.format(uri=parsed_uri)

            # Lets remove unnecessary crap so that the actual domain is all that's left
            while domain.count('.') > 1:
                domain = domain.partition('.')[2]
                
            print(domain)
            if i%2 == 0:
                source = "Very Respectable Authority Says So"
                sourceUrl = "http://www.google.com/"
                foo = "true"
            else:
                foo = "false"
                source = "Underpants Gnomes LLC"
                sourceUrl = "http://www.google.com/"
            jsonDicts['response'].append({"url":urlParam,"sourceUrl":sourceUrl, "source":source, "isFake":foo})
            i = i + 1
            
        

        
        return Response(jsonDicts)
