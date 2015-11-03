import redis
import boto.dynamodb
from django.shortcuts import render

from . import models
from django.conf import settings

r_server = redis.Redis('localhost')
r_server.set('counter', models.PageView.objects.count())


def home(request):
    return render(request, 'counter/home.html', {})


def count_db(request):
    models.PageView.objects.create()
    views = models.PageView.objects.count()
    return render(request, 'counter/db.html', {'views': views})


def count_cache(request):
    r_server.incr('counter')
    cached_views = r_server.get('counter')
    return render(request, 'counter/cache.html', {'cached_views': cached_views})

def count_dynamo(request):
    conn = boto.dynamodb.connect_to_region('us-east-1', 
                                           aws_access_key_id=settings.DYNAMODB_SESSIONS_AWS_ACCESS_KEY_ID, 
                                           aws_secret_access_key=settings.DYNAMODB_SESSIONS_AWS_SECRET_ACCESS_KEY)
    table =  conn.get_table('sessions')
    item = table.get_item(hash_key='counter')
    start_count = item['count']
    item['count'] = start_count + 1
    item.put()
    dynamo_views = item['count']
    return render(request, 'counter/dynamo.html', {'dynamo_views': dynamo_views})
