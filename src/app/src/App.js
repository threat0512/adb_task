import './App.css';
import { useState, useEffect } from 'react';

export function App() {
  const [todos, setTodos] = useState([]);
  const [todoInput, setTodoInput] = useState('');
  
  // api url for the todos
  const API_URL = 'http://localhost:8000/todos/';

  useEffect(() => {
    fetchTodos();
  }, []);

  // function to fetch the todos from the db
  const fetchTodos = async () => {
    try {
      const response = await fetch(API_URL);
      const data = await response.json();
      setTodos(data);
    } catch (err) {
      console.error('Error fetching todos:', err);
    }
  };

  // function to handle the form submission
  const handleSubmit = async (e) => {
    e.preventDefault();
    
    const trimmedInput = todoInput.trim();
    if (!trimmedInput) {
      alert('Todo cannot be empty');
      return;
    }
    
    try {
      // send the todo to the db
      const res = await fetch(API_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ todo: trimmedInput }),
      });
      
      // get the response from the db
      const data = await res.json();
      
      // if the response is not ok, show the error
      if (!res.ok) {
        alert(data.error || 'Failed to create todo');
        return;
      }
      
      // clear the input and fetch the todos
      setTodoInput('');
      fetchTodos();
    } catch (err) {
      // error while creating todo
      alert('Failed to create todo');
      console.error('Error creating todo:', err);
    }
  };

  return (
    <div className="App">
      <div>
        <h1>List of TODOs</h1>
        <ul>
          {todos.map((item, index) => (
            <li key={index}>{item.todo}</li>
          ))}
        </ul>
      </div>
      <div>
        <h1>Create a ToDo</h1>
        <form onSubmit={handleSubmit}>
          <div>
            <label htmlFor="todo">ToDo: </label>
            <input
              type="text"
              id="todo"
              value={todoInput}
              onChange={(e) => setTodoInput(e.target.value)}
            />
          </div>
          <div style={{ marginTop: "5px" }}>
            <button type="submit">Add ToDo!</button>
          </div>
        </form>
      </div>
    </div>
  );
}

export default App;
