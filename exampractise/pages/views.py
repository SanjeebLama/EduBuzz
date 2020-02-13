from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request,'pages/index.html')

def browse(request):
	return render(request,'pages/browse.html')

def contacts(request):
	return render(request,'pages/contacts.html')

def subject(request,subject):
	keyword= subject
	return render(request,'pages/subject.html')

def quiz(request, subject):
	keyword=subject
	return render(request,'pages/quiz.html')