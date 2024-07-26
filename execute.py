import csscompressor

import re

def parse_variables(lines):
    variables = {}
    for line in lines:
        match = re.match(r'^\$(\w+):\s*(.+)$', line)
        if match:
            var_name, var_value = match.groups()
            variables[var_name] = var_value
    return variables

def replace_variables(line, variables):
    for var_name, var_value in variables.items():
        line = line.replace(f'${var_name}', var_value)
    return line

def compile(input_code):
    lines = input_code.split('\n')
    variables = parse_variables(lines)
    output = []
    indent_level = 0
    indent_stack = []
    inside_block = False

    for line in lines:
        stripped_line = line.strip()
        if stripped_line and not stripped_line.startswith('$'):
            current_indent = len(line) - len(stripped_line)
            if current_indent > indent_level:
                indent_stack.append('{' * ((current_indent - indent_level) // 4))
            elif current_indent < indent_level:
                while indent_stack and indent_level > current_indent:
                    output.append(indent_stack.pop() + '\n}')
                    indent_level -= 4

            if current_indent == indent_level:
                stripped_line = replace_variables(stripped_line, variables)
                if stripped_line.endswith(':'):
                    output.append(' ' * current_indent + stripped_line[:-1] + ' {\n')
                    indent_stack.append(' ' * (current_indent + 4))
                    indent_level += 4
                elif stripped_line == '}':
                    while indent_stack and indent_level > 0:
                        output.append(indent_stack.pop() + '\n}')
                        indent_level -= 4
                elif ':' in stripped_line:
                    output.append(' ' * current_indent + stripped_line + ';\n')
                else:
                    output.append(' ' * current_indent + stripped_line + ';\n')

    while indent_stack:
        output.append(indent_stack.pop() + '\n}')

    code = ''.join(output).strip()
    minified_css = csscompressor.compress(code)
    return minified_css
