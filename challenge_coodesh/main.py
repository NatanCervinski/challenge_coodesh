from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def index():
    return {
        "message": "Back-end Challenge 2021 :medal: - Space Flight News"
    }
