from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return self.title

    # def create(self):
    #     return f"{self.title} creation successful."
    
    # def filter(self):
    #     return f"title={self.title}, author={self.author}, publication_year={self.publication_year}."
    
    # def update(self):
    #     return f"{self.title} updated successful."
    
    # def delete(self):
    #     return f"{self.title} deleted."
        