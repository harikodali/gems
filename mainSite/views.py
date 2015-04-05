from django.shortcuts import render_to_response, render
from mainSite.models import *
import json
from django.http import HttpResponse
from django.template import RequestContext, loader, Context
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from .databaseManager import getCandidateDetail,addCandidate

# Create your views here.
def logged(request):
	return render(request, 'main_page.html')

def register(request):
	if request.method == 'POST':
		form = CandidateForm(request.POST)
		if form.is_valid():
		    form.save()
		    data = form.CharField(label = 'Username')
		    return HttpResponse(json.dumps(data), content_type="application/json")
		    #return HttpResponseRedirect('/main')
		else:
		    return HttpResponse('error in registration')
    	else:
        	form = CandidateForm()
    	return render_to_response('registration_form.html',{'form': form}, context_instance=RequestContext(request))

def view_candidate(request):
    	candidate_i = Candidates.objects.all()
	candidate_data = {
		"candidate_detail" : candidate_i
	}
	return render_to_response('view_candidates.html', candidate_data, context_instance=RequestContext(request))

def candidateView(request,candidateName):
	candidateDetails = getCandidateDetail(candidateName)
	contextObj = Context({'candidateName':candidateName,'candidateDetails':candidateDetails})
	return render_to_response('test.html',contextObj)


