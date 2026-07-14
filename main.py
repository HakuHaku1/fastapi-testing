from fastapi import FastAPI, HTTPException

app = FastAPI()

@app.get("/")
def root():
    return {"Hello": "World"}

items = []

@app.post("/items")
def create_item(item: str):
    items.append(item)
    return items

@app.get("/items")
def limit_items(limit: int =10):
    return items[:limit]

@app.get("/items/{item_id}")
def get_items(item_id: int) -> str:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code=404, detail="Item not found")