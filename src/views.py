from django.http import HttpResponse

def sync_view(request):
    return HttpResponse('Sync')


async def async_view(request):
    return HttpResponse('Async')


async def fake_async_view_with_blocking(request):
    time.sleep(5)
    return HttpResponse("Vista async mal implementada: bloqueó el event loop.")
