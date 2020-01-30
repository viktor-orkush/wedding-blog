from django.http import Http404, JsonResponse
from contact.forms import ContactForm
from contact.telegram_notification import send_message


def contact_form(request):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'result': 'success', 'message': '<strong>Ваша заявка принята.</strong> '
                                                       'Мы свяжимся с Вами в ближайшее время!'}
            name = request.POST.get("user")
            phone = request.POST.get("phone")
            message = request.POST.get("message")
            message_text = "Новый запрос на сайте " + "\n Имя " + name + "\n Телефон " + phone + "\n Сообщение: " + message
            send_message(message_text)
        else:
            print(form)
            context = {'result': 'error'}
        return JsonResponse(context)
    else:
        raise Http404
