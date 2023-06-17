from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
import snscrape.modules.twitter as sntwitter


def index(request):
    username = ''
    content = []
    # con_date = []
    tweet_count = ''
    if request.method == 'GET':
        username = name = request.GET.get('username')
        tweet_count = int(request.GET.get('tweet_count'))
    
    query = f'from:{username}'
    tweets = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets.append(tweet)
        if i+1 == tweet_count:
            break

    # for n in tweets:
    #     content.append(n.user.username)
    #     content.append(n.content)
    #     content.append(n.date)
    #     content.append(n.likeCount)


    context ={
        'username':username,
        'tweet_count':tweet_count,
        'tweets':tweets,
        'content':tweets,

    }


    return render(request, 'index.html', context)
# Create your views here.
