from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("yam-peleg/Hebrew-Mistral-7B")
model = AutoModelForCausalLM.from_pretrained("yam-peleg/Hebrew-Mistral-7B")

input_text = "שלום! מה שלומך היום?"
input_ids = tokenizer(input_text, return_tensors="pt")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
