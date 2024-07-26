import csscompressor

def compile(code):
    minified_css = csscompressor.compress(code)
    return minified_css