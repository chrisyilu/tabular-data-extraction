from transformers import BertTokenizer, BertForTokenClassification
from torch.nn import Softmax
import torch

# load pre-trained BERT model and tokenizer
model_name = "bert-base-uncased"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForTokenClassification.from_pretrained(model_name)

# give tabular format
text = "Tabular data: Product | Price\n Item1  | $20\n Item2  | $30"

# tokenize and convert text to input format
tokens = tokenizer(text, return_tensors="pt")
inputs = tokens["input_ids"]
outputs = model(**tokens)

# apply softmax to classification
softmax = Softmax(dim=2)
probs = softmax(outputs.logits)

# threshold for considering a token as part of a table
# to be tuned
threshold = 0.75

# extract table-related information
table_entities = []
for token, prob in zip(tokens["input_ids"][0], probs[0]):
    # assuming '1' corresponds to the 'O' class for table entities
    if prob[1] > threshold:
        table_entities.append(token)

# decode tokens to get corresponding words
table_words = tokenizer.decode(table_entities)
print("Extracted Table Words:", table_words)
