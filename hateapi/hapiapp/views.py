from django.shortcuts import render

# Create your views here.
from hapiapp.models import FakeNews, FakeSite, SentimentData

from hapiapp.serializers import FakeNewsSerializer, FakeSiteSerializer, SentimentDataSerializer
from rest_framework import generics
from rest_framework.response import Response
from urllib.parse import urlparse

class SentimentList(generics.ListAPIView):
    queryset = SentimentData.objects.all()
    serializer_class = SentimentDataSerializer

    def list(self, request, *args, **kwargs):
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1: 
            return None

        urlParamList = query_dict.getlist("url")
        jsonDicts = {"response":[]}
        jsonDicts['response'].append({"url":"url", "containsHateSpeech":""})

        return Response(jsonDicts)
        
class FakeNewsList(generics.ListAPIView):
    # This is the fake news site data we have in the DB
    queryset = FakeSite.objects.all()

    serializer_class = FakeSiteSerializer

    # Here we construct a JSON response
    def list(self, request, *args, **kwargs):
        # Check if the domain is classified as a fake news site in out db
        # If it is, return the data from DB, else return None
        def amIFake(urlParam):
            #parsed_uri = urlparse(urlParam)
            #domain = parsed_uri.netloc
          
            if urlParam.startswith("http"):
                pass
            else:
                urlParam = "http://" + urlParam

            parsed_uri = urlparse(urlParam)
            domain = parsed_uri.netloc
            # Let's remove unnecessary crap so that the actual domain is all that's left
            while domain.count('.') > 1:
                domain = domain.partition('.')[2]
           
        
            filteredSet = self.queryset.filter(site__icontains=domain)
            if len(filteredSet) > 0 and domain != "twitter.com":
                return filteredSet
            else:
                return None

        # HTTP GET parameters are here
        query_dict = self.request.query_params
        query_keys = query_dict.keys()
        if len(query_keys) != 1:
            return None
    
        query_filters = []
        custom_filters = []

        # We want to go through all the URL -parameters
        urlParamList = query_dict.getlist("url")

        jsonDicts = {"response":[]}
        i = 0
        for urlParam in urlParamList:
            fakeData = amIFake(urlParam)
                       
            # Site is not fake, woohoo!
            if fakeData == None:
                source = ""
                sourceUrl = ""
                foo = "false"
            else: # It's a fake!
                foo = "true"
                source = fakeData.all()[0].sourcename
                sourceUrl = fakeData.all()[0].sourceurl
            jsonDicts['response'].append({"url":urlParam,"sourceUrl":sourceUrl, "source":source, "isFake":foo})
            i = i + 1
        
        return Response(jsonDicts)


