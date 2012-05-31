from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

from models import ItemAgenda
from forms import FormItemAgenda

def index(request):
	itens = ItemAgenda.objects.all().order_by('data')
	total = ItemAgenda.objects.count()
	return render_to_response('index.html', {'itens': itens, 'total': total})

def novo(request):
    if request.method == 'POST':
        form = FormItemAgenda(request.POST, request.FILES)
        
        if form.is_valid():
            dados = form.cleaned_data
            item = ItemAgenda(
                data=dados['data'],
                hora = dados['hora'],
                titulo = dados['titulo'],
                descricao = dados['descricao'],
                local = dados['local'])
            item.save()
            
            return render_to_response('salvo.html', {})
        
    else:
        form = FormItemAgenda()
        
    return render_to_response('novo.html', {'form': form}, context_instance=RequestContext(request))

def exibir(request, num_item):
    item = get_object_or_404(ItemAgenda, pk=num_item)
    return render_to_response('exibir.html', {'item': item})

def remover(request, num_item):
    item = get_object_or_404(ItemAgenda, pk=num_item)
    item.delete()
    return render_to_response('removido.html')
