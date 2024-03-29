from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Plat 
from .serializers import * 
# Create your views here.

@api_view(['GET', 'POST'])
def plat_list(request):
    """
    List  plat, or create a new plat.
    """
    if request.method == 'GET':
        data = []
        nextPage = 1
        previousPage = 1
        plats = Plat.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(plats, 10)
        try:
            data = paginator.page(page)
        except PageNotAnInteger:
            data = paginator.page(1)
        except EmptyPage:
            data = paginator.page(paginator.num_pages)
        serializer = PlatSerializer(data,context={'request': request} ,many=True)
        if data.has_next():
            nextPage = data.next_page_number()
        if data.has_previous():
            previousPage = data.previous_page_number()

        return Response({'data': serializer.data , 'count': paginator.count, 'numpages' : paginator.num_pages, 'nextlink': '/api/plats/?page=' + str(nextPage), 'prevlink': '/api/plats/?page=' + str(previousPage)})

    elif request.method == 'POST':
        serializer = PlatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def plat_detail(request, pk):
    """
    Retrieve, update or delete a plat instance.
    """
    try:
        plat = Plat.objects.get(pk=pk)
    except Plat.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlatSerializer(plat,context={'request': request})
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlatSerializer(plat, data=request.data,context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        plat.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
