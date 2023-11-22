from transformers import pipeline; 

classifier = pipeline('summarization', model="facebook/bart-large-cnn")

ARTICLE = """ Message brokers and queues play a crucial role in modern software architecture, enabling asynchronous communication between different components of a system. One powerful tool in this domain is Amazon Simple Queue Service (SQS), a highly durable queue in the cloud provided by Amazon Web Services (AWS). In this article, we will explore the fundamental concepts of message brokers, delve into the capabilities of AWS SQS, and understand its various use cases and limitations.
"""

print(classifier(ARTICLE, max_length=130, min_length=30, do_sample=False))