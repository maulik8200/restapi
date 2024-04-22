from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import APIView
from .serializer import *

# Create your views here.

class BookApi(APIView):
    def get(self,request):
        tasksdata = Tasks.objects.all()
        taskser = tasksSerializer(tasksdata,many=True)
        return Response({"data":taskser.data})
    
    def post(self,request):

        ser_data =  tasksSerializer(data=request.data)
       
        if not ser_data.is_valid():
          return Response({"message":"something went wrong","errors":ser_data.errors})
        ser_data.save()
        return Response({"userdata":ser_data.data,"message":"Task inserted"})


    def put(self,request):
        try:
            id = request.data['id']
            data = Tasks.objects.get(pk=id)
            
            ser_data = tasksSerializer(data,request.data)
            ser_data.is_valid(raise_exception=True)
            ser_data.save()
            return Response({"message":"Data updated successfully"})
        
        except Exception as e :
           return Response({"error":"User Not Found"})
    def delete(self,request):
        try:
            id = request.data['id']
            data = Tasks.objects.get(pk=id)
            data.delete()
            return Response({"message":"Delete Successfully"})
        except:
            return Response({"Error":"Something Wrong"})