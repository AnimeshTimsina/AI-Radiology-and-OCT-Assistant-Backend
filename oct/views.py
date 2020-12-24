from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import OCT_Image
from .serializers import OCT_Image_Serializer
from django.conf import settings
from django.http import HttpResponse
import numpy as np
import cv2
import os
from .models import OCT_Image
from rest_framework.decorators import api_view

@api_view(['GET'])
def OCT_DownloadSample_View(request):
    if request.method == 'GET':
        zip_file = open('data/Sample OCT Images.zip', 'rb')
        response = HttpResponse(zip_file, content_type='application/zip')
        response['Content-Disposition'] = 'attachment; filename=sample_oct_images.zip'
        return response

class OCT_Upload_View(APIView):
    def post(self,request,format=None):
        serializer = OCT_Image_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            relative_url = serializer['image'].value          
            absolute_url = os.path.join(settings.MEDIA_ROOT,relative_url)
            full_url_with_domain = request.build_absolute_uri(absolute_url)
            relative_url_without_slash = relative_url[1:]
            try:
                img_array = cv2.imread(relative_url_without_slash, cv2.IMREAD_GRAYSCALE)
                new_img = cv2.resize(img_array,(settings.OCT_IMG_SIZE, settings.OCT_IMG_SIZE))         
                X = []  
                X.append(new_img)
                X = np.array(X).reshape(-1, settings.OCT_IMG_SIZE, settings.OCT_IMG_SIZE, 1)
                X = X/255.0
                predictions = settings.OCT_MODEL.predict([X])
                defect_in_percentage = [value*100 for value in predictions[0]]
                
                defect_output = {}
                count=0
                for category in settings.OCT_CATEGORIES:
                    defect_output.update({
                        category : defect_in_percentage[count]
                    })
                    count = count + 1
                output = settings.OCT_CATEGORIES[np.argmax(predictions[0])]
                uploaded = OCT_Image.objects.order_by('-id')[0]
                uploaded.defect_type = output
                uploaded.save()
                response = Response(
                    {
                        "message":"Image processed successfully",
                        "result":output,
                        "status": status.HTTP_200_OK,
                        "image_url":full_url_with_domain,
                        "heatmap_image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/1/11/Test-Logo.svg/783px-Test-Logo.svg.png",
                        "defect_percentage":defect_output,
                        "output_download_url": ""
                    }
            )
            except:
                response = Response(
                    {
                        "message":"Uploaded image is not valid",
                        "status":status.HTTP_400_BAD_REQUEST,              
                    }
                )
            response.headers = "Set-Cookie", "HttpOnly;Secure;SameSite=Strict"
            return response
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


