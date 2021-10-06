from django.shortcuts import render
from contact.models import critic
from django.contrib import messages

# Create your views here.
def index(request):
    if request.method=='POST':
        name = request.POST['name']
        email = request.POST['email']
        question = request.POST['question']
        if len(name)<2 or len(email)<3 or len(question)<4:
            messages.error(request,'Please fill all fields')
        else:
            index = critic(critic_name=name, critic_email=email, critic_question=question)
            index.save()
            messages.success(request, 'Successfully Submitted')
    return render(request,'contact/contact.html')