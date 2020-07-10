from django.shortcuts import render
from searchApp.documents import NeighborDocument


def search_view(request):
    q = request.GET.get('q')
    basePath = "/static/searchApp/"

    if q:
        posts = NeighborDocument.search().query("match", master_pi=q)
        for post in posts:
            post["url"] = basePath + post["similar_url"] + ".jpg"

    else:
        posts = ''

    return render(request, 'searchApp/searchApp.html', {'posts': posts})
