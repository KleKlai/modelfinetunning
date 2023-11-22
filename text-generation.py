from transformers import pipeline

generator = pipeline("text-generation", model="distilgpt2")

res = generator(
    "Today we will focus on developing ai on how to",
    max_length=30,
    num_return_sequences=5,
)

print(res)