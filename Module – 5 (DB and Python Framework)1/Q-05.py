#Q-05 What is a QuerySet? Write program to create a new Post object in database:
'''
A QuerySet is a collection of database queries used to retrieve data from the database.

QuerySet allows you to filter, order, and manipulate data before retrieving it from the database.
'''
from .models import Post

post=Post.objects.create(title='Post Title', content='This is post content')
post.save()