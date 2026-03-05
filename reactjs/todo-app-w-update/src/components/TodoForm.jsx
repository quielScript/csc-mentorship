import { Plus } from "lucide-react";
import { useState } from "react";

function TodoForm({ onAddTodo }) {
	const [todo, setTodo] = useState("");

	function handleFormSubmit(e) {
		e.preventDefault();

		const newTodo = {
			todo,
			id: crypto.randomUUID(),
			isCompleted: false,
		};

		onAddTodo(newTodo);
		setTodo("");
	}

	return (
		<form className="mb-6" onSubmit={handleFormSubmit}>
			{/* FORM TITLE */}
			<h1 className="text-center mb-5 text-xl font-bold">TODO APP</h1>

			<div className="flex items-center justify-center gap-2">
				{/* TODO INPUT */}
				<input
					type="text"
					placeholder="Add a todo..."
					className="border border-black rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-purple focus:border-purple"
					value={todo}
					onChange={(e) => setTodo(e.target.value)}
				/>
				<button
					type="submit"
					className="cursor-pointer bg-purple text-white font-medium py-2 px-4 rounded-md focus:outline-purple focus:outline-offset-2"
				>
					<Plus className="text-white" />
				</button>
			</div>
		</form>
	);
}

export default TodoForm;
