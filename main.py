from fastapi import FastAPI 
from fastapi import Query
from fastapi.responses import PlainTextResponse
from jsmin import jsmin
from fastapi.middleware.cors import CORSMiddleware
from execute import compile

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)


def readfile():
    with open('execjs/javascript.js', 'r') as file:
        file_contents = file.read()
    return file_contents

@app.get("/", response_class=PlainTextResponse)
async def bridge():
    minified_js = jsmin(readfile())
    return minified_js

@app.get("/compile/")
async def compile_css(var: str = Query(...)):
    print(f"Received CSS content: {var}")
    return compile(var)