# GenAI-Based Code Analysis & Documentation Assistant

A GenAI-powered assistant that performs static code analysis and automatically generates high-quality documentation using pre-trained large language models.

## Key Features
- Static code analysis using Python AST
- Automated documentation generation
- Prompt-engineered GenAI outputs
- No dataset or model training required
- REST API built with Flask

## Technology Stack
- Python
- Flask
- Hugging Face Transformers
- Prompt Engineering
- Git

## API Endpoint

### POST /analyze

#### Request Body
```json
{
  "code": "def add(a, b): return a + b"
}
