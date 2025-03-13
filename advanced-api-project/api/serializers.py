from rest_framework import serializers
from .models import Author, Book
from datetime import datetime


#  Book model serializer that inherits from Modelserializer
#  with a validation of publication year using django built-in validate function and datetime.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


    def validate(self, publication_year):
        if publication_year > datetime.now:
            raise serializers.ValidationError('Date can not be in the future.')
        return publication_year
    

# An Author serializer that inherits from Modelserializer 
# with a nested BookSerializer that handles one to many relationship
# between an author and books
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author
        fields = ['name', 'books']
        