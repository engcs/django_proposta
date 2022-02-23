from django.contrib import admin
from .models import Cliente, Proposta #, DescricaoPagamento, Pagamento
# Register your models here.
class PropostaAdmin(admin.ModelAdmin):

    # def get_changelist(self, request, **kwargs):
    #     return TotalChangeList
    #
    # inlines = [
    #             PagamentoInline
    #           ]
    list_display = ['cliente', 'data', 'pago', 'valor', ] # 'imprimir',
    search_fields = ['cliente__nome']
    list_filter = ['cliente__nome', 'data', 'situacao']
    # list_editable = ['valor']
    list_per_page = 30
    save_on_top = True

class ClienteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Proposta, PropostaAdmin)
admin.site.register(Cliente, ClienteAdmin)