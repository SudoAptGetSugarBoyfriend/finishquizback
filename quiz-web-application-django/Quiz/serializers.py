from rest_framework import serializers
from Quiz.models import QuesModel

class QuizApiSerializer(serializers.ModelSerializer):

	class Meta:
		model = QuesModel
		fields = '__all__'