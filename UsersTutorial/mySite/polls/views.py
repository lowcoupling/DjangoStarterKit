# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from polls.models import Poll
from polls.models import Choice
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render

#see https://docs.djangoproject.com/en/dev/topics/auth/
@login_required
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    return render_to_response('polls/index.html', {'latest_poll_list':latest_poll_list}, context_instance=RequestContext(request))

@login_required
def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})

def vote_view(request,poll_id):
    p = get_object_or_404(Poll, pk=poll_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'polls/detail.html', {
            'poll': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,))) 