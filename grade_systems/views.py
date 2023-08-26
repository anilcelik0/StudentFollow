from django.shortcuts import render
from .models import User, Lessons, ExamGrade
from .permissions import IsAuthenticationorReadonly, OnlyAdminToWrite

#API Libraries
from rest_framework import viewsets
from .serializers import  UserSerializer, LessonsSerializer, ExamGradeSerializer
from rest_framework.response import Response

# Filterset Librares
from django_filters import FilterSet, DateTimeFromToRangeFilter, rest_framework as filters

# Create your views here.

# Filterset

class UserFilter(FilterSet):
    
    class Meta:
        model = User
        fields = ['is_teacher','is_student']


class LessonsFilter(FilterSet):
    
    class Meta:
        model = Lessons
        fields = ['lesson_name','teacher','students']


class ExamGradeFilter(FilterSet):
    
    class Meta:
        model = ExamGrade
        fields = ['student','lesson']


#API
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = UserFilter
    permission_classes = (OnlyAdminToWrite,)
    

class LessonsViewSet(viewsets.ModelViewSet):
    queryset = Lessons.objects.all()
    serializer_class = LessonsSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = LessonsFilter
    permission_classes = (IsAuthenticationorReadonly,)
 
    
class ExamGradeViewSet(viewsets.ModelViewSet):
    queryset = ExamGrade.objects.all()
    serializer_class = ExamGradeSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ExamGradeFilter
    permission_classes = (IsAuthenticationorReadonly,)


# for oken
from .serializers import MyTokenObtainPairSerializer
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer