from django.contrib import admin

from .models import Proposal, Status


class ProposalAdminInline(admin.TabularInline):
    model = Status


class ProposalAdmin(admin.ModelAdmin):
    """Proposal admin model."""
    list_display = ('mahasiswa', 'judul', 'get_status')
    fields = ('mahasiswa', 'judul')
    inlines = [ProposalAdminInline, ]

    def get_status(self, obj):
        return obj.status_set.last()


admin.site.register(Proposal, ProposalAdmin)