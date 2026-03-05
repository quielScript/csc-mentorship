import TodoItem from "./TodoItem";

function TodoList({
	todos,
	onCompleteTodo,
	onDeleteTodo,
	setIsUpdateTodoFormOpen,
}) {
	return (
		<ul className="flex flex-col divide-y divide-gray-400">
			{todos.map((todo) => (
				<TodoItem
					todo={todo}
					key={todo.id}
					onCompleteTodo={onCompleteTodo}
					onDeleteTodo={onDeleteTodo}
					setIsUpdateTodoFormOpen={setIsUpdateTodoFormOpen}
				/>
			))}
		</ul>
	);
}

export default TodoList;
