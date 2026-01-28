import ast

def extract_functions(code: str):
    parsed_tree = ast.parse(code)
    functions = []

    for node in ast.walk(parsed_tree):
        if isinstance(node, ast.FunctionDef):
            functions.append({
                "name": node.name,
                "parameters": [arg.arg for arg in node.args.args],
                "source_code": ast.get_source_segment(code, node)
            })

    return functions
