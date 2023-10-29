# #!  HttpResponse :
# #?
# from django.http import HttpResponse
# def hello_world(request):
#     return HttpResponse("Hello, World!")

# #!  HttpResponseRedirect:
# #? פונקציה זו משמשת לניתוב משתמש לדף אחר.
# #? היא מקבלת את המסלול (URL) לו המשתמש יועבר, 
# #? ומחזירה תוצאה שמכילה את ההפניה אל המסלול הזה
# from django.http import HttpResponseRedirect
# from django.urls import reverse
# def redirect_to_home(request):
#     # מפנה את המשתמש לדף הבית
#     return HttpResponseRedirect(reverse('home'))


# #!  JsonResponse :
# #? פונקציה זו משמשת ליצירת תגובה בפורמט JSON.
# #? היא מקבלת מידע בפורמט JSON
# #? ומחזירה תוצאה שמכילה את המידע בפורמט JSON.

# from django.http import JsonResponse

# def get_json_data(request):
#     data = {'name': 'Alice', 'age': 30}
#     return JsonResponse(data)

# #! FileResponse:

# #?
# from django.http import FileResponse
# from django.conf import settings
# from django.shortcuts import get_object_or_404
# from models import MyModel
# def download_file(request, id):
#     my_object = get_object_or_404(MyModel, pk=id)
#     file_path = my_object.file_field.path
#     return FileResponse(open(file_path, 'rb'))


# #! StreamingHttpResponse :

# #?
# from django.http import StreamingHttpResponse

# def stream_large_file(request):
#     # מחזיר תוכן גדול באמצעות פרוצדורת זריקת תוכן
#     def file_iterator(file_path, chunk_size=8192):
#         with open(file_path, 'rb') as f:
#             while True:
#                 chunk = f.read(chunk_size)
#                 if not chunk:
#                     break
#                 yield chunk

#     file_path = 'path/to/large_file.zip'
#     response = StreamingHttpResponse(file_iterator(file_path))
#     response['Content-Type'] = 'application/octet-stream'
#     response['Content-Disposition'] = 'attachment; filename="large_file.zip"'
#     return response

# #! JsonResponse with Custom Status Code:

# #?
# from django.http import JsonResponse

# def custom_status_code(request):
#     data = {'message': 'Custom status code', 'status_code': 418}
#     return JsonResponse(data, status=418)

# #! 404 Error Handling:

# #?
# from django.http import Http404

# def custom_404(request):
#     raise Http404("This page does not exist")


# #! StreamingHttpResponse with Large Data Processing:

# #?
# from django.http import StreamingHttpResponse

# def large_data_processing(request):
#     # מפעיל עיבוד של מידע גדול ומחזיר StreamingHttpResponse
#     def process_large_data():
#         for i in range(1, 100000):
#             yield str(i) + '\n'

#     return StreamingHttpResponse(process_large_data())

# #! XMLHttpResponse:

# #?
# from django.http import HttpResponse
# from xml.etree.ElementTree import Element, tostring

# def xml_response(request):
#     # מחזיר תגובה בתבנית XML
#     root = Element('root')
#     element = Element('message')
#     element.text = 'This is an XML response'
#     root.append(element)
#     response = HttpResponse(tostring(root), content_type='application/xml')
#     return response

# #! 404 Error Page with Template:
# #?
# from django.http import Http404
# from django.shortcuts import render

# def custom_404_template(request):
#     # מציג תבנית דף שגיאת 404 מותאמת אישית
#     raise Http404("This page does not exist")

# def handler404(request, exception):
#     return render(request, 'custom_404.html', status=404)




# #! Content-Type and Headers:
# #? 

# from django.http import HttpResponse

# def custom_headers(request):
#     # מוסיף כותרות נוספות לתגובה
#     response = HttpResponse("Custom Headers")
#     response['X-Custom-Header'] = 'Custom Value'
#     response['Cache-Control'] = 'no-cache'
#     return response
