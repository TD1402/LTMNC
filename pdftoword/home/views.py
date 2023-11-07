import os
from django.conf import settings
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.views.decorators.http import require_POST
from pdf2docx import Converter
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import ConvertedFile
import uuid
from django.contrib.auth.decorators import user_passes_test

def generate_short_code():
    return str(uuid.uuid4())[:5]

@csrf_protect
@require_POST
def pdftoword(request):
    file = request.FILES.get('pdf_file')
    if file and file.name.endswith('.pdf'): 
        short_code = generate_short_code()
        converted_file = ConvertedFile(pdf_file=file, short_code=short_code, user=request.user)
        converted_file.save()


        filename = os.path.splitext(file.name)[0]
        docx_filename = filename.replace(" ", "_")
        docx_file_path = os.path.join(settings.MEDIA_ROOT, 'docx_files', docx_filename + '.docx')


        try:
            pdf_converter = Converter(converted_file.pdf_file.path, docx_file_path)
            pdf_converter.convert()

            converted_file.docx_file.name = os.path.join('pdf_files', docx_filename + '.docx')  # Add '.docx' extension here
            converted_file.save()

            return JsonResponse({'short_code': short_code})
        except Exception as e:
            return HttpResponse('Conversion failed or file not found', status=500)
    else:
        return HttpResponse('Invalid PDF file provided', status=400)

def convert_form(request):
    user = request.user if request.user.is_authenticated else None
    return render(request, 'index.html', {'user': user})


# def converted_file_list(request):
#     converted_files = ConvertedFile.objects.all()
#     return render(request, 'converted_file_list.html', {'converted_files': converted_files})
@user_passes_test(lambda u: u.is_superuser, login_url='/login/')  # Only allow admins
def converted_file_list_admin(request):
    converted_files = ConvertedFile.objects.all()
    return render(request, 'converted_file_list.html', {'converted_files': converted_files})

def converted_file_list_user(request):
    converted_files = ConvertedFile.objects.filter(user=request.user)
    return render(request, 'converted_file_list.html', {'converted_files': converted_files})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('convert_form')  # Redirect to the 'convert_form' page upon successful login
        else:
            # Handle login failure, e.g., display an error message
            return render(request, 'login.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'login.html')


def downloadpage(request, pk):
    converted_file = ConvertedFile.objects.get(short_code=pk)
    d = os.path.splitext(converted_file.docx_file.name)[0]
    prefix_to_remove = "pdf_files\\"
    if d.startswith(prefix_to_remove):
        d = d[len(prefix_to_remove):]
    print(d)
    return render(request, 'dq.html', {'hi': converted_file,'h':d})

