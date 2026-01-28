from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from datetime import date
from .models import Speech

def submit_speech(request):
    if request.method == 'POST':
        speech_date = request.POST['date']
        
        # Check if date is already taken
        if Speech.objects.filter(date=speech_date).exists():
            messages.error(request, f'The date {speech_date} is already booked. Please choose another date.')
            return redirect('submit')
        
        speech = Speech(
            name=request.POST['name'],
            program=request.POST['program'],
            date=speech_date,
            title=request.POST.get('title', 'TBD'),
            content=request.POST.get('content', ''),
            add_later='addLater' in request.POST
        )
        
        # Handle picture upload
        if 'picture' in request.FILES:
            speech.picture = request.FILES['picture']
        
        speech.save()

        send_mail(
            subject='New BHM Speech Date Reserved',
            message=f"A new speech date has been reserved:\n\nName: {request.POST['name']}\nProgram: {request.POST['program']}\nDate: {speech_date}\nTitle: {request.POST.get('title', 'TBD')}\n\nCheck the admin panel for details.",
            from_email=None,
            recipient_list=['jjoshuaj300@gmail.com'],
        )

        messages.success(request, 'Your speech date has been reserved! Please remember to go to the front office on that day at 10:05')
        return redirect('submit')

    # Get all booked dates in February
    booked_dates = Speech.objects.filter(date__month=2).values_list('date', flat=True)
    booked_dates = [d.isoformat() for d in booked_dates]
    
    # Get all speeches that are ready to display (have content/picture and not marked "add_later")
    speeches = Speech.objects.filter(
        date__month=2,
        add_later=False
    ).exclude(
        content='',
        picture=''
    ).order_by('date')
    
    context = {'booked_dates': booked_dates, 'speeches': speeches}
    return render(request, 'speeches/submit.html', context)
