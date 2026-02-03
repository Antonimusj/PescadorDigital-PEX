from django.contrib import messages
from django.core.exceptions import ValidationError
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from django.views.generic.edit import CreateView
from cadastros.models import Pescadores
from cadastros.forms import PescadoresForm
from cadastros.validators import validar_cpf


# Página inicial com campo para digitar o CPF
def pag_abertura(request):
    context = {}
    if request.method == "POST":
        cpf = request.POST.get('cpf')
        if cpf:
            try:
                validar_cpf(cpf)  # Valida CPF antes de qualquer consulta
                try:
                    # Se o CPF já existe, redireciona para a lista filtrada
                    pescador = Pescadores.objects.get(cpf=cpf)
                    return redirect(f'/listaPescadores/?q={cpf}')
                except Pescadores.DoesNotExist:
                    # Se CPF não existe, redireciona para o cadastro preenchendo o CPF automaticamente
                    return redirect(f'/cadPescadores/?cpf={cpf}')
            except ValidationError:
                # Flag usada no template para exibir erro de CPF inválido
                context['cpf_invalido'] = True

    # Renderiza a página inicial
    return render(request, "index.html", context)


# View para cadastro de novos pescadores (CreateView)
class PescadoresCad(CreateView):
    model = Pescadores
    form_class = PescadoresForm
    template_name = "cadastros/cadastro.html"
    success_url = reverse_lazy("cadPescadores")

    # Preenche automaticamente o CPF no formulário se vier pela URL
    def get_initial(self):
        initial = super().get_initial()
        cpf = self.request.GET.get('cpf')
        if cpf:
            initial['cpf'] = cpf
        return initial

    # Mensagem de sucesso ao cadastrar
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Pescador cadastrado com sucesso!")
        return response


# View para listar pescadores (ListView)
class PescadorList(ListView):
    model = Pescadores
    template_name = "cadastros/lista.html"
    context_object_name = "pescadores"
    paginate_by = 10  # 10 por página

    # Filtra por CPF se houver parâmetro "q" na URL
    def get_queryset(self):
        cpf = self.request.GET.get("q")
        if cpf:
            return Pescadores.objects.filter(cpf__icontains=cpf)
        return Pescadores.objects.all()


# View para editar pescadores (UpdateView)
class PescadoresEdit(UpdateView):
    model = Pescadores
    form_class = PescadoresForm
    template_name = "cadastros/editar.html"
    success_url = reverse_lazy("listaPescadores")

    # Mensagem de sucesso ao editar
    def form_valid(self, form):
        messages.success(self.request, "Pescador atualizado com sucesso!")
        return super().form_valid(form)


# View para deletar pescadores (DeleteView)
class PescadoresDelete(DeleteView):
    model = Pescadores
    template_name = "cadastros/deletar.html"
    success_url = reverse_lazy("listaPescadores")

    # Mensagem de sucesso ao deletar
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Pescador deletado com sucesso!")
        return super().delete(request, *args, **kwargs)
