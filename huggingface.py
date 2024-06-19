import requests

API_URL = "https://api-inference.huggingface.co/models/sentence-transformers/all-MiniLM-L6-v2"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()

source = ['Data Scientist I or II - Card Fraud Analytics']	
output = query({
	"inputs": {
		"source_sentence": f"{source[0]}",
		"sentences": [
                        "Data Analyst",
                        "Risk Analyst",
                        "Data Science Analyst",
                        "Business Analyst",
                        "Senior Data Science Analyst",
                        "Senior Business Analyst",
                        "Data Scientist",
                        "Data Scientist I or II"
                        "Junior Data Scientist",
                        "Senior Data Scientist"
                    ]
	},
})

output.sort(reverse=True)
result = map(lambda x: x * 100,output)
final_result = list(result)
print(final_result)
if final_result[0] > 70:
    print("yes")