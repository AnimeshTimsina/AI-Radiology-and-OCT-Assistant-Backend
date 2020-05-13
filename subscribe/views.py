from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from radiology_and_oct_backend.settings import EMAIL_HOST_USER,EMAIL_RECEIVER
import re 

regex_email = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'



class SendEmailView(APIView):
    def post(self,request,format=None):
        subject = "Enquiry for AI Radiology and OCT Assistant"
        obtained_data = request.data['to_send']
        name = obtained_data['name']
        email = obtained_data['email']
        phone = obtained_data['phone']
        message  = obtained_data['message']
        if ((not name) or (not email) or (not phone) or (not message)):
            return Response({
                'error': 'Please, fill all the fields',
            },status=status.HTTP_400_BAD_REQUEST)
        elif(re.search(regex_email,email)):  
            return Response({
                'error': 'Email is invalid',
            },status.HTTP_400_BAD_REQUEST)      

        elif len(name) > 50 or len(email) >50:
            return Response({
                'error': 'Please, enter valid information',
                'status':status.HTTP_400_BAD_REQUEST
            },status.HTTP_400_BAD_REQUEST) 
        else:      
            final_mail = "Name : " + str(name) + "\n" + "Email : "  + str(email) + "\n" + "Phone : " + str(phone) + "\n" + "Message: " + "\n" + str(message)
            recepient = EMAIL_RECEIVER
            send_mail(subject, 
                final_mail, EMAIL_HOST_USER, [recepient], fail_silently = False)
            response = Response(
                {
                    'messsage':'Message sent successfully',
                    'status':status.HTTP_200_OK
                }
            )
            return response