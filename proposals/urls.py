from django.urls import path
from .views import ProposalCreateView, ProposalDetailView

urlpatterns = [
    path('add/', ProposalCreateView.as_view(), name='proposal_add'),
    path('<int:pk>/', ProposalDetailView.as_view(), name='proposal_detail'),
]