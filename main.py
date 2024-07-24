from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
from jsmin import jsmin
import os

app = FastAPI()

def readfile():
    with open('execjs/javascript.js', 'r') as file:
        file_contents = file.read()
    return file_contents

@app.get("/", response_class=PlainTextResponse)
async def bridge():
    minified_js = jsmin(readfile())
    return minified_js
