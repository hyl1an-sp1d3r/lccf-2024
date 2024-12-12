import sys
import os
import json
import csv
import time
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/minilm-uncased-squad2"

arr = []
#assigns filename with command line argument
filename = sys.argv[1]
#opens file
file = open(filename, 'r')
text = file.read()
file.close()

j_file = sys.argv[2]
f = open(j_file, 'r')
data = json.load(f)
f.close()

start = time.perf_counter()

for i in data:
	query = i["question"]
	nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)

	question = query
	context = text
	res = nlp(question=question, context=context)
	#print(res)
	#diction = dict(question = query, answer_given = res['answer'], score = res['score'], answer_desired['desired answer'])

	arr.append({"Question": query, "Answer Given": res['answer'], "Score": res['score'], "Actual Answer": i['desired answer']})
	model = AutoModelForQuestionAnswering.from_pretrained(model_name)
	tokenizer = AutoTokenizer.from_pretrained(model_name)

end = time.perf_counter()

time_elapsed = end - start
print("Time taken: " + str(time_elapsed) + " seconds")

filename_json = filename.replace('.txt', '.json')
filename_csv = filename.replace('.txt', '.csv')

path_json = 'tables/minilm/json_results' + filename_json
path_csv = 'tables/minilm/csv_results' + filename_csv

field_names = ["Question", "Answer Given", "Score", "Actual Answer"]

with open(path_json, 'w') as fit:
        json.dump(arr, fit, indent=4)

with open(path_csv, 'w') as fitted:
        writer = csv.DictWriter(fitted, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(arr)
