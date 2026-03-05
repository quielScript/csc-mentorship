import { useState } from "react";
import TodoForm from "./components/TodoForm";
import TodoList from "./components/TodoList";
import UpdateTodoForm from "./components/UpdateTodoForm";

function App() {
	const [todos, setTodos] = useState([]);
	const [isUpdateTodoFormOpen, setIsUpdateTodoFormOpen] = useState(false);

	function handleAddTodo(newTodo) {
		setTodos((todos) => [...todos, newTodo]);
	}

	function handleCompleteTodo(todoId) {
		setTodos((todos) =>
			todos.map((todo) =>
				todo.id === todoId ? { ...todo, isCompleted: !todo.isCompleted } : todo
			)
		);
	}

	function handleDeleteTodo(todoId) {
		setTodos((todos) => todos.filter((todo) => todo.id !== todoId));
	}

	function handleUpdateTodo(todoId, newTodo) {
		setTodos((todos) =>
			todos.map((todo) =>
				todo.id === todoId ? { ...todo, todo: newTodo } : "todo"
			)
		);
	}

	return (
		<main className="min-h-dvh flex items-center justify-center">
			{/* MAIN CONTAINER */}
			<div className="border border-black p-5 rounded-md">
				{/* TODO FORM */}
				<TodoForm onAddTodo={handleAddTodo} />
				{/* TODO LIST */}
				<TodoList
					todos={todos}
					onCompleteTodo={handleCompleteTodo}
					onDeleteTodo={handleDeleteTodo}
					setIsUpdateTodoFormOpen={setIsUpdateTodoFormOpen}
				/>
			</div>

			{/* UPDATE TODO FORM */}
			{isUpdateTodoFormOpen ? (
				<UpdateTodoForm onUpdateTodo={handleUpdateTodo} />
			) : null}
		</main>
	);
}

export default App;
