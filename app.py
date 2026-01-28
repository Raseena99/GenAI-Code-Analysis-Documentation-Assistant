from flask import Flask, request, jsonify
from services.parser import extract_functions
from services.prompt_builder import build_prompt
from services.llm_client import generate_documentation

app = Flask(__name__)

@app.route("/analyze", methods=["POST"])
def analyze_code():
    data = request.get_json()
    code = data.get("code")

    if not code:
        return jsonify({"error": "Source code is required"}), 400

    functions = extract_functions(code)
    response = []

    for function in functions:
        prompt = build_prompt(function)
        documentation = generate_documentation(prompt)

        response.append({
            "function_name": function["name"],
            "generated_documentation": documentation
        })

    return jsonify(response), 200


if __name__ == "__main__":
    app.run(debug=True)
