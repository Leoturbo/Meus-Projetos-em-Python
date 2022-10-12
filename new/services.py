from config import API_KEY, endpoint, country
import request

def services(category='general'):
	new_api = NewsApiClient(API_KEY)
	articles = new_api.get_top_headlines(endpoint, country='br')


	result = json.loads(articles)
  	articles = None


    return result.articles
