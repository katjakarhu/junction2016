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
        def amIFake(urlParam):
            parsed_uri = urlparse(urlParam)
            domain = '{uri.netloc}'.format(uri=parsed_uri)
            # Lets remove unnecessary crap so that the actual domain is all that's left
            while domain.count('.') > 1:
                domain = domain.partition('.')[2]
                
            print(domain)
        
            filteredSet = self.queryset.filter(site__contains=domain)
            if len(filteredSet) > 0:
                return filteredSet
            else:
                filteredSet = self.queryset.filter(site__contains=parsed_uri)
                return None


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
            fakeData = amIFake(urlParam)
            
            if fakeData == None:
                source = ""
                sourceUrl = ""
                foo = "false"
            else:
                foo = "true"
                source = fakeData.all()[0].sourcename
                sourceUrl = fakeData.all()[0].sourceurl
            jsonDicts['response'].append({"url":urlParam,"sourceUrl":sourceUrl, "source":source, "isFake":foo})
            i = i + 1
            
        

        
        return Response(jsonDicts)


