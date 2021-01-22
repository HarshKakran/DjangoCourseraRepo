from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.views import View
from .models import Question, Choice

# Create your views here.

'''class IndexView(View):
    def get(self, request):
        latest_question_list = Question.objects.order_by('-pub_date')[:5]
        context = {'latest_question_list': latest_question_list}
        #output = ', '.join([q.question_text for q in latest_question_list])
        return render(request,
                      'poll/index.html',
                      context = context)
'''

def owner(request):
    return HttpResponse("Hello, world. 7f018eb7 is the polls owner.")
"""
class DetailView(View):

    '''try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")'''
    '''OR'''
    def get(self,request, question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'poll/detail.html', {'question': question})

class ResultsView(View):
    def get(self, request ,question_id):
        question = get_object_or_404(Question, pk=question_id)
        return render(request, 'poll/result.html', {'question': question})
"""
class IndexView(generic.ListView):
    template_name = 'poll/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'poll/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'poll/result.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('poll:results', args=(question.id,)))
