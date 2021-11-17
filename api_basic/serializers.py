from rest_framework import serializers
from .models import Article


# class ArticleSerializer(serializers.Serializer):
#     title = serializers.CharField()
#     author = serializers.CharField()
#     email = serializers.EmailField()
#     date  = serializers.DateTimeField()

#     def create(self,validate_date):
#         return Article.objects.create(validate_date)

#     def update(self,instance,validate_date):
#         instance.title = validate_date.get('title',instance.title)
#         instance.author = validate_date.get('author',instance.author)
#         instance.email = validate_date.get('email',instance.email)
#         instance.date = validate_date.get('date',instance.date)
#         instance.save()
#         return instance
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # fields = ['id','title','author','email']
        fields ='__all__'
