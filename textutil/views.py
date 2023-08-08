# mannually
from django.shortcuts import HttpResponse,render

def index(request):
    dict1 = {"name":"Ranjeet","loc":"chd"}
    return render(request,"index.html",dict1)
    #return HttpResponse("<h1>hello world python <h2>")

def analyze(request):
    djtext = request.POST.get('text',"default")
    removepuch = request.POST.get('removepunc','off')
    fullcaps= request.POST.get("fullcaps","off")
    newlineremover = request.POST.get("newlineremover","off")
    extraspaceremover=request.POST.get("extraspaceremover","off")

    if removepuch =='on':
        punc = """!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"""
        str1 = ''
        for char in djtext:
            if char not in punc:
                str1 = str1+char
        
        params ={"purpose":"Removing Punctuation","analyzed_text":str1}
        djtext = str1
      #  return render (request,"analyze.html",params)
          
    if fullcaps=="on":
        str1 = ''
        for char in djtext:
            str1 = str1+char.upper()
        
        params ={"purpose":"UpperCase ","analyzed_text":str1}
      #  return render(request,"analyze.html",params)
        djtext = str1
       
    
    if (newlineremover =='on'):
        str1 = ''
        for char in djtext:
            if char != "\n" and char !='\r':
                str1+=char
      
        params ={"purpose":"Removed NewLines ","analyzed_text":str1}
        djtext=str1
    #    return render(request,"analyze.html",params)
    
    
    if extraspaceremover=="on":
        str1 =''
        for i,c in enumerate(djtext):
            if not(djtext[i]==" " and djtext[i+1]==" "):
                str1 = str1+c
        
        params ={"purpose":"Removing Punctuation","analyzed_text":str1}
        #return render (request,"analyze.html",params)
        djtext = str1

    if(removepuch !='on'and fullcaps!="on"and newlineremover!='on' and extraspaceremover!="on"):
           return HttpResponse("please select any operation and try again ")
    return render (request,"analyze.html",params)





def about(request):
    return HttpResponse("""
                        
                        <button><a href ="/">back</a></button></form>
                        <h1> navbar </h1>
                        <a href ="https://www.youtube.com/">youtube</a><br>
                        <a href = "https://www.linkedin.com/feed/">linkedin</a>
                        <br>
                        <a href = "https://www.facebook.com/">Facebook</a>
                       """ )