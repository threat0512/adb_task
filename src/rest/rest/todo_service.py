import logging
from pymongo.errors import PyMongoError

logger = logging.getLogger(__name__)

# todo service class to handle todo operations
class TodoService:
    def __init__(self, collection):
        self.collection = collection
    # function to get all the todos from the db
    def get_all_todos(self):
        try:
            todos = self.collection.find()
            result = []
            for todo in todos:
                result.append({"todo": todo["todo"]})
            logger.info(f"Got {len(result)} todos")
            return result
            
        # db error while fetching todos
        except PyMongoError as e:
            logger.error(f"Database error while fetching todos {e}")
            raise Exception("Failed to fetch todos from database")
    
    # function to create a new todo in the db
    def create_todo(self, todo_text):
        try:
            todo = {"todo": todo_text}
            
            if self.collection.find_one(todo):
                logger.warning(f"Duplicate todo found {todo_text}")
                raise ValueError("Todo already exists")
            
            self.collection.insert_one(todo)
            logger.info(f"Created todo: {todo_text}")
            
            return {"todo": todo_text}
            
        # value error while creating todo
        except ValueError:
            raise
        # db error while creating todo
        except PyMongoError as e:
            logger.error(f"Database error while creating todo {e}")
            raise Exception("Failed to create todo in database")
    
    # function to validate the todo text
    def validate_todo_text(self, todo_text):
        if not todo_text or not isinstance(todo_text, str):
            raise ValueError("Todo text must be a string")
        
        todo_text = todo_text.strip()
        # todo cannot be empty
        if len(todo_text) == 0:
            raise ValueError("Todo cannot be empty")
        
        # todo cannot exceed 100 characters
        if len(todo_text) > 100:
            raise ValueError("Todo cannot exceed 100 characters")
        
        return todo_text

