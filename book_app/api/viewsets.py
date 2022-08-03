from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters import rest_framework as filters
from .serializers import BookSerializer
from book_app.models import Book
from rest_framework.authentication import TokenAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated


class BookFilter(filters.FilterSet):
    #title=filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model=Book
        fields={
            'name':['icontains'],
            'author':['exact','icontains'],
            'price':['lte','gte','exact']
        }


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_class=BookFilter
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    @action(methods=['get'],detail=False)
    def newest(self,request):
        newest=self.get_queryset().order_by('id').last()
        serializer=self.get_serializer_class()(newest)
        print(serializer.data)
        return Response(serializer.data)



