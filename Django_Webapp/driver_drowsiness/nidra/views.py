from django.shortcuts import render
from django.http import StreamingHttpResponse
from nidra.camera import VideoCamera


# Create your views here.

def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def developer(request):
    return render(request, 'developers.html')


def detection_api(request):
    return render(request, 'camera.html', {'isApiUsed': 1})


def detection_model(request):
    return render(request, 'camera.html', {'isApiUsed': 0})


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed_api(request):
    return StreamingHttpResponse(gen(VideoCamera(1)), content_type='multipart/x-mixed-replace; boundary=frame')


def video_feed_model(request):
    print("come to page")
    return StreamingHttpResponse(gen(VideoCamera(0)), content_type='multipart/x-mixed-replace; boundary=frame')
