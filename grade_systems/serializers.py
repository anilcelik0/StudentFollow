from rest_framework import serializers
from .models import User, Lessons, ExamGrade


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'password', 'date_of_birth', 'date_of_registration', 'is_teacher', 'is_student')
        
    
    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            date_of_birth=validated_data['date_of_birth'],
            date_of_registration=validated_data['date_of_registration'],
            is_teacher=validated_data['is_teacher'],
            is_student=validated_data['is_student']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
        

class LessonsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lessons
        fields = "__all__"
        
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_teacher=True), write_only=True)
    students = serializers.SerializerMethodField('_get_students')
    
    def _get_students(selF, obj):
        data = {}
        students = obj.students.all()
        
        for student in students:
            student_data = {
                student.id: {
                    "name": student.first_name,
                    "surname": student.last_name,
                    "username": student.username,
                }
            }
            data.update(student_data)
            
        return data


class ExamGradeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = ExamGrade
        fields = "__all__"

    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_student=True), write_only=True)



#for token
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)

        token['username'] = user.username
        return token