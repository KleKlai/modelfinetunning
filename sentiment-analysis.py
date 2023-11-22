from transformers import pipeline; 

classifier = pipeline('sentiment-analysis')

res = classifier("ahhh mubalik paka dadto?")

print(res)

# from transformers import pipeline; 
# from transformers import AutoTokenizer, AutoModelForSequenceClassification

# classifier = pipeline('sentiment-analysis')

# res = classifier("ahhh mubalik paka dadto?")

# print(res)

# model_name = "distilbert-base-uncased-finetuned-sst-2-english"
# model = AutoModelForSequenceClassification.from_pretrained(model_name)
# tokenizer = AutoTokenizer.from_pretrained(model_name)

# classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)

# res = classifier("ahhh mubalik paka dadto?")

# print(res)