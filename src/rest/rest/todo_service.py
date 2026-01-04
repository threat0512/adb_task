import logging
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)


class TodoService:
    def __init__(self, collection):
        self.collection = collection
    
    def get_all_todos(self):
        try:
            todos = self.collection.find()
            result = []
            for todo in todos:
                result.append({"todo": todo["todo"]})
            logger.info(f"Got {len(result)} todos")
            return result
            
        except PyMongoError as e:
            logger.error(f"Database error while fetching todos {e}")
            raise Exception("Failed to fetch todos from database")
    
    def create_todo(self, todo_text):
        try:
            todo = {"todo": todo_text}
            
            if self.collection.find_one(todo):
                logger.warning(f"Duplicate todo found {todo_text}")
                raise ValueError("Todo already exists")
            
            self.collection.insert_one(todo)
            logger.info(f"Created todo: {todo_text}")
            
            return {"todo": todo_text}
            
        except ValueError:
            raise
        except PyMongoError as e:
            logger.error(f"Database error while creating todo {e}")
            raise Exception("Failed to create todo in database")
    
    def validate_todo_text(self, todo_text):
        if not todo_text or not isinstance(todo_text, str):
            raise ValueError("Todo text must be a string")
        
        todo_text = todo_text.strip()
        
        if len(todo_text) == 0:
            raise ValueError("Todo cannot be empty")
        
        if len(todo_text) > 100:
            raise ValueError("Todo cannot exceed 100 characters")
        
        return todo_text

