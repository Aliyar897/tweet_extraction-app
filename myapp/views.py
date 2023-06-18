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
        username = request.GET.get('username')
        if username == '' or username == None:
            username = 'No User Found, Aliyar403324241'
        tweet_count = int(request.GET.get('tweet_count') or 0)
    print(type(username))
    print(type(tweet_count))
    query = f'from:{username}'
    tweets = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
        tweets.append(tweet)
        print('Hello')
        if tweet_count == 0:
            tweets = []
            tweets.append('No tweet found')
            break
        elif i+1 == tweet_count:
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
