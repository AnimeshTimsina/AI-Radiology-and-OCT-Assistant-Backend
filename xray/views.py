from django.http import HttpResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def XRAY_DownloadSample_View(request):
    if request.method == 'GET':
        zip_file = open('data/Sample XRAY Images.zip', 'rb')
        response = HttpResponse(zip_file, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=sample_xray_images.zip'
        return response