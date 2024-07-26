# CSSPLUS
*css for haters*
## Introduction
CSSPlus is a tool to design CSS like Python without using {, ;, or }

## Motivation
Because CSS is a styling language, I want to avoid the semicolons and {} symbols.

## quick start
```html
<script src="https://cssplus.onrender.com"></script>
<style>
body:
    font-family: Arial, sans-serif
    background-color: #f0f0f0
    margin: 0
    padding: 0
</style>
```

> [!WARNING]
> Indent 0. no spaces or tabs
> 
> ![nospace](https://github.com/user-attachments/assets/e57483f8-7cd1-42e9-97e0-2ed3c4a82cf5)

## Example code
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>cssplus Website</title>
    <script src="https://cssplus.onrender.com"></script>
    <style>
body:
    font-family: Arial, sans-serif
    background-color: #f0f0f0
    margin: 0
    padding: 0

header:
    background-color: #4CAF50
    color: white
    text-align: center
    padding: 1em 0

nav:
    margin: 0
    padding: 1em
    background-color: #333

    a:
        color: white
        text-decoration: none
        margin: 0 1em

main:
    padding: 2em

footer:
    background-color: #333
    color: white
    text-align: center
    padding: 1em 0
    position: absolute
    bottom: 0
    width: 100%

    </style>
</head>
<body>
    <header>
        <h1>cssplus example Website</h1>
    </header>
    <nav>
        <a href="#">Home</a>
        <a href="#">About</a>
        <a href="#">Contact</a>
    </nav>
    <main>
        <h2>Main Content</h2>
        <p>This is a paragraph of text in the main content area.</p>
    </main>
    <footer>
        <p>&copy; 2024 compile studio. All rights reserved.</p>
    </footer>
</body>

</html>

```

