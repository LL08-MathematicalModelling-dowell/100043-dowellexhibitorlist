from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    try:
        session_id = request.GET.get("session_id", None)
        if session_id:
            request.session["session_id"] = session_id
            # url = 'https://100014.pythonanywhere.com/api/userinfo/'
            # res = requests.post(url, data={"session_id": session_id})
            return render(request, 'exhibitors/index.html', {'session_id': session_id})

        return redirect("https://100014.pythonanywhere.com/?redirect_url=https://100043.pythonanywhere.com")
    except:

        return redirect("https://100014.pythonanywhere.com/?redirect_url=https://100043.pythonanywhere.com/")


def add_data(request):
    try:

        return render(request, 'exhibitors/form1.html')

    except:
        return redirect("https://100014.pythonanywhere.com/?redirect_url=https://100043.pythonanywhere.com/")
