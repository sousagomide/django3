from typing import Any

from django.views.generic import TemplateView

from core.models import FuncionarioModel, ServicoModel


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = ServicoModel.objects.order_by('?').all()
        context['funcionarios'] = FuncionarioModel.objects.order_by('?').all()
        return context

