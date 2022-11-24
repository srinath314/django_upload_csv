import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage

from django.contrib import messages
# Create your views here.
def home(request):

    context={}

    if request.method == 'POST':
        uploaded_file = request.FILES['data_file']

        if uploaded_file.name.endswith('.csv'):
            #save the file in media
            #     
            savefile = FileSystemStorage()

            name = savefile.save(uploaded_file.name, uploaded_file)

            d = os.getcwd() #gets current directory
            file_dir = d+'\media\\'+name
        else: 
            messages.warning(request, 'file was not uploaded')


    return render(request, 'home.html')