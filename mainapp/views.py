from django.shortcuts import render

from django.http import HttpResponse

from django.views.generic import TemplateView


class ContactsView(TemplateView):
    template_name = 'mainapp/contacts.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['contacts'] = [
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'mail': 'geeklab@spb.ru',
                'adress': 'территория Петропавловская крепость, 3Ж',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'mail': 'geeklab@kz.ru',
                'adress': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
            },
            {
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'mail': 'geeklab@msk.ru',
                'adress': 'Красная площадь, 7, Москва, Россия',
            },
        ]
        return context_data
class CoursesListView(TemplateView):
    template_name = 'mainapp/courses_list.html'


class DocSiteView(TemplateView):
    template_name = 'mainapp/doc_site.html'


class IndexView(TemplateView):
    template_name = 'mainapp/index.html'



class LoginView(TemplateView):
    template_name = 'mainapp/login.html'


class NewsView(TemplateView):
    template_name = 'mainapp/news.html'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data["object_list"] = [
            {
                'title': 'Новость первая',
                'date': '2022-01-01',
                'preview': 'Превью к первой новости'
            },
            {
                'title': 'Новость вторая',
                'date': '2022-01-02',
                'preview': 'Превью ко второй новости'
            },
            {
                'title': 'Новость третья',
                'date': '2022-01-03',
                'preview': 'Превью к третьей новости'
            },
            {
                'title': 'Новость четвертая',
                'date': '2022-01-04',
                'preview': 'Превью к четвертой новости'
            },
            {
                'title': 'Новость пятая',
                'date': '2022-01-05',
                'preview': 'Превью к пятой новости'
            }
        ]


        return context_data