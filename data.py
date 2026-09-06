import datasets

data = []

def check_list(list):
    if list is None:
        return False
    elif list is not None:
        return True

dataset = datasets.load_dataset("Hello-SimpleAI/HC3", "all")


for item in range(200):
    row = dataset["train"][item]
    if check_list(row["human_answers"]) is False:
        continue
    else:
        data.append({"text": row["human_answers"][0], "label": 0})
    
    if check_list(row["chatgpt_answers"]) is False:
        continue
    else:
        data.append({"text": row["chatgpt_answers"][0], "label": 1})