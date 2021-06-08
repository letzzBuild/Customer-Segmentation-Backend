import re
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import DealSerializer

# Create your views here.
@api_view(['POST'])
def AddDeal(request):
    response = {"status":1 ,"message":""}
    serializer = DealSerializer(data=request.data)
    try:
        if serializer.is_valid():
          serializer.save()
          response['message'] = "Deal Added success and email notifications sent to respective customers"
        else:
            response['status'] = 0
            print(serializer.errors)
            response['message'] = "something went wrong check parameters in data"
    except Exception as e:
          print(e)
          response['status'] = 0
          response['message'] = str(e)

    finally:
        return Response(response)          
            
