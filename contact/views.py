from django.http import Http404, JsonResponse
from contact.forms import ContactForm


def contact_form(request):
    if request.is_ajax():
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            context = {'result': 'success', 'message': '<strong>Ваша заявка принята.</strong> '
                                                       'Мы свяжимся с Вами в ближайшее время!'}
        else:
            print(form)
            context = {'result': 'error'}
        return JsonResponse(context)
    else:
        raise Http404
