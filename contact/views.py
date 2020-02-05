from django.http import Http404, JsonResponse
from contact.forms import ContactForm
from contact.serializers import ContactSerializer
from contact.telegram_notification import send_message
from rest_framework.views import APIView
from django.middleware.csrf import get_token


# def contact_form(request):
#     if request.is_ajax():
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             context = {'result': 'success', 'message': '<strong>Ваша заявка принята.</strong> '
#                                                        'Мы свяжимся с Вами в ближайшее время!'}
#             name = request.POST.get("user")
#             phone = request.POST.get("phone")
#             message = request.POST.get("message")
#             message_text = "Новый запрос на сайте " + "\n Имя " + name + "\n Телефон " + phone + "\n Сообщение: " + message
#             send_message(message_text)
#         else:
#             print(form)
#             context = {'result': 'error'}
#         return JsonResponse(context)
#     else:
#         raise Http404

class CustomerAddContact(APIView):
    """
    DRF view API for contact form
    :param request: user, phone, message
    :return: success
    """
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            context = {'result': 'success',
                       'message': '<strong>Ваша заявка принята.</strong> '
                                  'Мы свяжемся с Вами в ближайшее время!'}
            name = request.data.get("user")
            phone = request.data.get("phone")
            message = request.data.get("message")
            message_text = "Новый запрос на сайте " + "\n Имя: " + name + "\n Телефон: " + phone + "\n Сообщение: " + message
            send_message(message_text)
        else:
            context = {'result': 'error'}
        return JsonResponse(context)


