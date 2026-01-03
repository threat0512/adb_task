from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json, logging, os
from pymongo import MongoClient

mongo_uri = 'mongodb://' + os.environ["MONGO_HOST"] + ':' + os.environ["MONGO_PORT"]
db = MongoClient(mongo_uri)['test_db']
todos = db['todos']

  
class TodoListView(APIView):

    def get(self, request):
        # Implement this method - return all todo items from db instance above.
        res = []
        for todo in todos.find():
            dict_todo = {"todo": todo["todo"]}
            res.append(dict_todo)
        return Response(res, status=status.HTTP_200_OK, content_type='application/json')
        
    def post(self, request):
        # Implement this method - accept a todo item in a mongo collection, persist it using db instance above.
        todo = { "todo": request.data.get("todo") }
        todos.insert_one(todo)
        return Response(True, status=status.HTTP_200_OK, content_type='application/json')

