from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="microsoft/phi-2",
    max_new_tokens=300
)

def generate_documentation(prompt: str) -> str:
    output = generator(
        prompt,
        do_sample=True,
        temperature=0.2
    )
    return output[0]["generated_text"]
