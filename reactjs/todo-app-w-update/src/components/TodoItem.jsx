import { SquarePen, Trash2 } from "lucide-react";

function TodoItem({
	todo,
	onCompleteTodo,
	onDeleteTodo,
	setIsUpdateTodoFormOpen,
}) {
	return (
		<li className="py-3">
			<div className="flex items-center justify-between gap-2">
				{/* LEFT SIDE */}
				<div className="flex items-center gap-2">
					<input
						type="checkbox"
						className="w-4 h-4 accent-purple cursor-pointer"
						onChange={() => onCompleteTodo(todo.id)}
					/>
					{/* TASK NAME */}
					<p className={!todo.isCompleted ? "" : "line-through"}>{todo.todo}</p>
				</div>

				{/* RIGHT SIDE */}
				<div className="flex items-center gap-2">
					<button className="cursor-pointer">
						<SquarePen className="text-gray-400" />
					</button>
					<button
						className="cursor-pointer"
						onClick={() => onDeleteTodo(todo.id)}
					>
						<Trash2 className="text-red-500" />
					</button>
				</div>
			</div>
		</li>
	);
}

export default TodoItem;
