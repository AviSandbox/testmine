from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from .models import Article
from datetime import datetime
from django.http import Http404
#from django.contrib.syndication.views import Feed

# Create your views here.
def index(request):
	post_list=Article.objects.all()
	return render(request,'index.html', {'post_list':post_list})
	#return render(request, 'index.html')
# did not in use yet (list)
def list(request):
	names=[]
	return render(request,'list.html',{'names':names})
def detail(request, id):
	try:
		post = Article.objects.get(id=str(id))
	except Article.DoesNotExist:
		raise Http404
	#str=("title=%s,category=%s, date_time=%s, content=%s"
	#	%(post.title, post.category, post.date_time,post.content))
	#return HttpResponse (str)
	#return HttpResponse (f'article detail with the id of {id}')
	return render(request, 'post.html',{'post':post})

def test(request):
    return render(request, 'test.html', {'current_time': datetime.now()})

#RSS

class RSSFeed(Feed):
	title="RSS feed-article"
	link="feeds/posts"
	description="RSS feed -blog posts"

	def items(self):
		return Article.objects.order_by('-date_time')
		

	def item_title(self,item):
		return item.title

	def item_pubdate(self, item):
		return item.add_date

	def item_description(self,item):
		return item.content
