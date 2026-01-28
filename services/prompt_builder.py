def build_prompt(function: dict) -> str:
    return f"""
You are a senior software engineer and technical writer.

Perform code analysis and generate professional documentation including:
1. A Python-style docstring
2. Function purpose
3. Parameter descriptions
4. Return value explanation
5. Example usage

Function Name: {function['name']}
Parameters: {function['parameters']}

Code:
{function['source_code']}
"""
