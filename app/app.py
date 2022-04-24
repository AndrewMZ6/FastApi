from fastapi import FastAPI

app = FastAPI()


# minimal app - get request
@app.get("/", tags = ["ROOT"])
async def root() ->dict:
	return {"Ping": "Pong"}

# Get --> read todo
@app.get("/todo", tags = ["todos"])
async def get_todos() -> dict:
	return {"data": todos}


# Post --> create todo
@app.post("/todo", tags = ["todos"])
async def create_todo(task: dict) -> dict:
	try:
		todos.append(task)
		return {"data":"successfull!"}
	except:
		return {"data":"something went wrong"}


# Put --> update todo
@app.put("/todo/{id}", tags = ["todos"])
async def update_todo(id:int, body: dict) -> dict:
	for todo in todos:
		if int(todo["id"]) == id:
			todo["Activity"] = body["Activity"]
			return {"data":"successfull!"}
	return{"data":"unsuccessfull!"}

# Delete --> delete todo
@app.delete("/todo/{id}", tags = ["todos"])
async def delete_todo(id:int) -> dict:
	for todo in todos:
		if int(todo["id"]) == id:
			todos.remove(todo)
			return {"data":f"the todo N {id} was remover succesfully {type(id)}"}


todos = [
		{"id":"1",
		"Activity": "puting things in order at my folders"
		},
		{
		"id":"2",
		"Activity": "make my radio access labs ready"
		}
]