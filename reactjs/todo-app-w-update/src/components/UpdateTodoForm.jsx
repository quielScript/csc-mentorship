function UpdateTodoForm() {
	return (
		<div className="absolute inset-0 bg-black/50 z-10">
			<div className="w-[500px] bg-white absolute top-1/2 left-1/2 -translate-1/2 z-20 p-5 rounded-md">
				<label htmlFor="todo">Update Todo</label>
				<input
					id="todo"
					type="text"
					placeholder="..."
					className="border border-black rounded-md py-2 px-4 focus:outline-none focus:ring-2 focus:ring-purple focus:border-purple w-full mb-5"
				/>

				<div className="flex justify-end gap-5">
					<button className="text-white bg-purple py-2 px-4 rounded-md cursor-pointer">
						Save
					</button>
					<button className="bg-gray-400 text-white py-2 px-4 rounded-md cursor-pointer">
						Cancel
					</button>
				</div>
			</div>
		</div>
	);
}

export default UpdateTodoForm;
