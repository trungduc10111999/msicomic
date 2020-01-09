from django.shortcuts import render

from comic.models import Comic, TableChap


def Home_view(request):
    object_list = Comic.objects.filter(name__in=['One Piece', 'One Punch Man'])
    object_left = Comic.objects.filter(name__in=['Dragon Ball', 'Conan'])

    item1 = Comic.objects.filter(name__in=['Doraemon'])
    item2 = Comic.objects.filter(name__in=['Conan'])

    itemUpdate = Comic.objects.filter(name__in=['Ô Long Viện', 'Boruto', 'Bleach', 'Attack On Titan'])
    list_comic = Comic.objects.filter(name__in=['Ô Long Viện', 'Yugi-Oh', 'Black Clover'])
    list_comic2 = Comic.objects.filter(name__in=['Đội Quân Nhí Nhố', 'Cardcaptor Sakura', 'Yai-Ba'])

    listTop = Comic.objects.filter(name__in=['Yai-Ba'])
    list_full_1 = Comic.objects.filter(name__in=['Yai-Ba'])
    list_full_2 = Comic.objects.filter(name__in=['Yai-Ba'])

    carousel = Comic.objects.filter(name__in=['Naruto'])
    carousel2 = Comic.objects.filter(name__in=['Naruto'])
    carousel3 = Comic.objects.filter(name__in=['Naruto'])

    return render(request, 'Home.html', {
        'object_list': object_list,
        'object_left': object_left,

        'item1': item1,
        'item2': item2,

        'itemUpdate': itemUpdate,
        'list_comic': list_comic,
        'list_comic2': list_comic2,

        'listTop': listTop,
        'list_full_1': list_full_1,
        'list_full_2': list_full_2,

        'carousel': carousel,
        'carousel2': carousel2,
        'carousel3': carousel3,

        'nav': 'home'
    })


def up18_view(request):
    list_comic_18cong = Comic.objects.filter(name__in=['Ô Long Viện', 'Yugi-Oh', 'Black Clover'])
    list_comic_18cong2 = Comic.objects.filter(name__in=['Yai-Ba', 'Attack On Titan', 'Black Clover'])
    list_comic_18cong3 = Comic.objects.filter(name__in=['Ô Long Viện', 'Cardcaptor Sakura', 'Black Clover'])
    return render(request, '18+.html', {
        'list_comic_18cong': list_comic_18cong,
        'list_comic_18cong2': list_comic_18cong2,
        'list_comic_18cong3': list_comic_18cong3,

        'nav': '18+'
    })


def Under18_view(request):
    list_comic_18tru = Comic.objects.filter(name__in=['Ô Long Viện', 'Yugi-Oh', 'Black Clover'])
    list_comic_18tru2 = Comic.objects.filter(name__in=['Ô Long Viện', 'Yugi-Oh', 'Black Clover'])
    list_comic_18tru3 = Comic.objects.filter(name__in=['Ô Long Viện', 'Yugi-Oh', 'Black Clover'])
    return render(request, '18-.html', {
        'list_comic_18tru': list_comic_18tru,
        'list_comic_18tru2': list_comic_18tru2,
        'list_comic_18tru3': list_comic_18tru3,

        'nav': '18-'
    })


def Detail_comic(request, comic_id):
    detail = Comic.objects.get(pk=comic_id)
    return render(request, 'OverView.html', {
        'detail': detail,

        'nav': 'OverView'
    })


def view_comic(request, tableChap_id):
    ViewComic = TableChap.objects.get(pk=tableChap_id)
    return render(request, 'view.html', {
        'ViewComic': ViewComic,

        'nav': 'view'
    })