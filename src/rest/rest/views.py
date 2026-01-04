from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

from .todo_service import TodoService
from .database import todos_collection

logger = logging.getLogger(__name__)

  
class TodoListView(APIView):

    def __init__(self):
        self.service = TodoService(todos_collection)

    def get(self, request):
        try:
            todos = self.service.get_all_todos()
            return Response(todos, status=status.HTTP_200_OK)
            
        except Exception as e:
            logger.error(f"Error getting todos {e}")
            return Response(
                {"error": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        
    def post(self, request):
        try:
            todo_text = request.data.get("todo")
            
            validated_text = self.service.validate_todo_text(todo_text)
            
            created_todo = self.service.create_todo(validated_text)
            
            return Response(created_todo, status=status.HTTP_201_CREATED)
            
        except ValueError as e:
            logger.warning(f"Validation error {e}")
            return Response(
                {"error": str(e)},
                status=status.HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            logger.error(f"Error in POST todo {e}")
            return Response(
                {"error": "Failed to create todo"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

