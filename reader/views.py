from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, Posts
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from insta.bot import run

def index(request):
	accounts = Account.objects.all()
	return HttpResponse(','.join([a.handle for a in accounts]))

def run_bot(request): 
	run(Account.objects.all())
	return HttpResponse('ok')

def insert_first_acc():
	print('running first')
	if len(Account.objects.all()) == 0:
		for handle in ['rcnaomono','pefabiodemelo','genipapos','omarcusboaventura','masculinidade.saudavel']:
			Account(handle=handle).save() 

insert_first_acc()
# run_bot('a')
 
def detail(request, question_id):
	# try:
	# 	question = Question.objects.get(pk=question_id)
	# except Question.DoesNotExist:
	# 	raise Http404("Question does not exist")
	question = get_object_or_404(Account, pk=question_id)
	return render(request, "polls/detail.html", {"question": question})
