from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.

monthly_challenges = {
    "january": "finish learning all the backend stuff",
    "february": "start learning dsa and finish it",
    "march": "finish learning all the theory subjects and become a complete computer science engineer",
    "april": "eat no meat for the entire month",
    "may": "minimize the frequency of smoking weed",
    "june": "start exercising",
    "july": "start reading books",
    "august": "learn about django in more depth",
    "september": "learn about clean code",
    "october": "learn about advanced object oriented design concepts",
    "november": "no shaving and nutting",
    "december": None #"trip to kasol"
}


def welcome(request):
    month_names = list(monthly_challenges.keys())
    return render(request=request, template_name="challenges/index.html",context=
    {
        "month_names": month_names
    })
    # unordered_list = "<ul>"
    # for month in month_names:
    #     generated_url = reverse(viewname="month-challenge", args=[month])
    #     list_item_string = f'<li><a href="{generated_url}">click here to see challenge for {month}</a></li>'
    #     unordered_list += list_item_string
    # unordered_list += "</ul>"
    # return HttpResponse(unordered_list)


def monthly_challenge_by_number(request, month):
    if month < 1 or month > 12:
        return HttpResponseNotFound("<h1>sorry month can only be in the range of between 1 and 12</h1>")
    else:
        # redirect_url = reverse(viewname="giri")
        # return HttpResponseRedirect(redirect_url)
        redirect_month = list(monthly_challenges.keys())[month - 1]
        redirect_url = reverse(viewname="month-challenge", args=[redirect_month]) # give the name of the url and the
        # value we want to send in the place holder in case it has any placeholder if it has no placeholder that is
        # the dynamic segment than it will automatically construct the full static url like the above example whose
        # url name is giri
        return HttpResponseRedirect(redirect_url)
        # return HttpResponseRedirect(f"/challenges/{redirect_month}")


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month.lower()]
    except KeyError:
        raise Http404()
        # this below approach also works but this is so common that that raise Http404() class
        #because it is a shortcut
        #rendered_error_page = render_to_string(template_name="404.html", context={
                #"invalid_text": month
            #})
        #return HttpResponseNotFound(rendered_error_page)
    # this render to string is actually the long way of doing the exact same thing can be done by the render function
    # which is shown below
    # html_code = render_to_string(template_name="challenges/challenge.html", context=
    # {
    #     "month_name": month,
    #     "challenge_text": challenge_text
    # })
    # return HttpResponse(html_code)
    return render(request=request, template_name="challenges/challenge.html", context=
    {
        "month_name": month,
        "challenge_text": challenge_text
    })
    # return HttpResponse(f"<h1>{challenge_text}</h1>")


# def show_ayush_details(request):
#     return HttpResponse("hello there this is the details page about ayush giri here and "
#                         "i'm learning django it is quite a new task and challenging for me"
#                         "but i'm loving this challenge and i want to grow even more as a programmer"
#                         "and become a software engineer and maybe become a python and sql professor"
#                         "in the new upcoming sessions")
