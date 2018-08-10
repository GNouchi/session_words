from django.shortcuts import render , redirect, HttpResponse

def index(request):
    return render(request,"index.html")

def submit(request):
    temp ={}
    if 'arr' not in request.session.keys():
        request.session['arr']=[]
    temp_list =request.session['arr'] 
    if request.method=='POST' and request.POST['word'] != '':
        for x in request.POST:
            if x !='csrfmiddlewaretoken':
                temp[x] = request.POST[x]
        temp_list.append(temp)
        request.session['arr']= temp_list  
        print('*'*50)
        print(request.session['arr'])
        print('*'*50)
        # print(request.session.keys())
    return redirect('/')

def reset(request):
    print('------------------------- flushing-----------------------------')
    request.session.flush()
    return redirect('/')    