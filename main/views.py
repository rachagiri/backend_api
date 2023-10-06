# what kind of view we want to show
from rest_framework import generics,permissions,pagination,viewsets
#import the serializers in our views
from . import serializers
# import model
from . import models


# Create your views here.
# VendorList returns all the sellers
# from generices we want list API view, it will return data as alist
# change the “ListAPIView” to "ListCreateAPIView", it is responsible for creating the data and adding the data 

class VendorList(generics.ListCreateAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # we can add as many permission we want
    # permission_classes=[permissions.IsAuthenticated]


# VendorDetail returns all the details of the vendors
# from generices we want RetrieveAPIView, it will return data 
# change “RetrieveAPIView” to RetrieveUpdateDestroy”, which is responsible, for fetching, updating and destroying the single data 


class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # we can add as many permission we want
    # permission_classes=[permissions.IsAuthenticated]


# ProductList returns all the list of the products
class ProductList(generics.ListCreateAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer


# ProductList returns all the list of the products
class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer



# CustomerList returns all the CCustomer
class CustomerList(generics.ListCreateAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer


# CustomerDetail returns all the details of the Customers
class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerDetailSerializer


# OrderList returns all the sellers
class OrderList(generics.ListCreateAPIView):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    pagination_class=pagination.LimitOffsetPagination


# OrderDetail returns all the details of the Customers
class OrderDetail(generics.ListAPIView):
    # queryset = models.OrderItems.objects.all()
    serializer_class = serializers.OrderDetailSerializer

    def get_queryset(self):
        order_id=self.kwargs['pk']
        order=models.Order.objects.get(id=order_id)
        order_items=models.OrderItems.objects.filter(order=order)

        return order_items



# CustomerAddress retusn customer address
class CustomerAddressViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.CustomerAddressSerializer
    queryset=models.CustomerAddress.objects.all()


# ProductRatingViewSet returns customer product reviews and ratings
class ProductRatingViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.ProductRatingSerializer
    queryset=models.ProductRating.objects.all()


# category list API view
class CategoryList(generics.ListCreateAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategorySerializer


# category detail API view
class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.ProductCategory.objects.all()
    serializer_class = serializers.CategoryDetailSerializer



