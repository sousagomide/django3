from django.contrib import admin

from core.models import CargoModel, FuncionarioModel, ServicoModel


@admin.register(CargoModel)
class CargoAdmin(admin.ModelAdmin):
    list_display = ('cargo', 'ativo')

@admin.register(ServicoModel)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('servico', 'descricao', 'icone', 'ativo')

@admin.register(FuncionarioModel)
class FuncionarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cargo', 'bio', 'instagram', 'twitter', 'ativo')
