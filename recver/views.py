from django.shortcuts import render
from django.views import View

class CameraDisplay(View):
    def get(self,request):
        return render(request,'recver/camera_display_page.html')
    def post(self,request):
        pass