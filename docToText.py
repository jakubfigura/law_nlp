import textract
import os
import pandas as pd

def doc_to_string(file_path):
    text = textract.process(file_path)
    return text.decode('utf-8')

rulings = []
folder = os.listdir("your_path_to_folder")
i = 1
for file in folder:
    rulings.append(doc_to_string("your_path_to_folder" + f"{file}"))
    print(f"{file} number {i}")
    i+=1

data = {"raw_rulings": rulings}
df = pd.DataFrame(data = data)
df.to_csv("TK0409.csv")