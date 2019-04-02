import requests, re, random,json
from bs4 import BeautifulSoup

def main():
	url = "https://conversationstartersworld.com/would-you-rather-questions/"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'lxml')
	wyr_questions = [re.sub('\?$', '', q.text.strip()) for q in soup.findAll('p')[7:200]]

	question_regex = re.compile('would you rather (.*?) or (.*)', re.IGNORECASE)
	question_list = []
	for q in wyr_questions:
		search = question_regex.search(q)
		if search:
			option1, option2 = search.group(1).capitalize(), search.group(2).capitalize()
			vote1 = random.randint(20, 80)
			vote2 = 100 - vote1
			question_list.append({
				"options": [
					{ "text": option1, "votes": vote1 },
					{ "text": option2, "votes": vote2 }
				]
			})

	with open('questions.json', 'w') as f: 
		json.dump(question_list, f)

if __name__ == '__main__':
	main()