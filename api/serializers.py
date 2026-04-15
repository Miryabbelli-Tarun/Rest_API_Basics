from rest_framework import serializers

from students.models import Marks, Student

class MarksSerialier(serializers.ModelSerializer):
    class Meta:
        model=Marks
        fields='__all__'
        extra_kwargs = {
            'student': {'read_only': True}
        }


class StudentSerializer(serializers.ModelSerializer):
    # students=MarksSerialier(many=True,read_only=True)
    marks=MarksSerialier(many=True)
    class Meta:
        model=Student
        fields='__all__'

    def create(self, validated_data):
        marks_data=validated_data.pop('marks')
        student=Student.objects.create(**validated_data)
        for marks in marks_data:
            Marks.objects.create(student=student,**marks)
        return student
