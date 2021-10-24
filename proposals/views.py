from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from proposals.models import Proposal, Status

class ProposalCreateView(CreateView):
    model = Proposal
    template_name = 'proposals/proposal_form.html'
    fields = ['judul']

    def form_valid(self, form):
        self.obj = form.save(commit=False)
        self.obj.mahasiswa = self.request.user
        self.obj.save()
        Status.objects.create(
            proposal=self.obj,
            status='Submit judul'
        )
        return super(ProposalCreateView, self).form_valid(form)


class ProposalDetailView(DetailView):
    model = Proposal
    template_name = 'proposals/proposal_detail.html'
