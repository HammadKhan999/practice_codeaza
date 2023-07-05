from fastapi import FastAPI
app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World!"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

@app.get("/users/{user_id}")
def read_user(user_id: int, q: str = None, skip: int = 0, limit: int = 10):
    return {"user_id": user_id, "q": q, "skip": skip, "limit": limit}
