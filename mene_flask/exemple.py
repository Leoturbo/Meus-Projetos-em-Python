
def buscar_dados():
    request = requests.get("https://api.github.com/events")
    todos = json.loads(request.content)
    print(todos)
    print(todos[0]['titulo'])



def buscar_dados_id(id):
    request = requests.get(f"https://api.github.com/events?id={id}")
    todo = json.loads(request.content)
    meme_large = todo["preview"][-2]
	subreddit = todos["subreddit"]
