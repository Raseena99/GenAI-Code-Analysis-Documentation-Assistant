# GenAI-Based Code Analysis & Documentation Assistant – Architecture

## Overview
The system performs static code analysis using Python AST and leverages a pre-trained GenAI model to generate structured documentation.

## Workflow
1. User submits source code via REST API
2. AST parser extracts functions and metadata
3. Prompt builder constructs a structured GenAI prompt
4. LLM generates documentation
5. Flask returns JSON response

## Design Principles
- No dataset or model training
- Prompt-driven intelligence
- Modular and extensible design
- Rapid prototyping focused
