from fastapi import FastAPI

app = FastAPI()  # call the module


@app.get("/")  # decorator
def root():  # Mainfunction
    return {"message": "Hello World"}
