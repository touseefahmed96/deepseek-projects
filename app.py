from fastapi import FastAPI

from text_summarizer import summarize_text

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/summarize/")
def read_item(text: str):
    return {"summary": summarize_text(text)}
