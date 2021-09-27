from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

CustomUser = get_user_model()


STATUS = (
    ('judul_submitted', 'Submit judul'),
    ('judul_approved', 'Judul approved'),
    ('proposal_submitted', 'Submit proposal'),
    ('proposal_revised', 'Submit revisi proposal'),
    ('proposal_dosen_ok', 'Proposal disetujui dosen pembimbing'),
    ('proposal_kaprodi_ok', 'Proposal disetujui kaprodi'),
    ('proposal_dosen_no', 'Proposal tidak disetujui dosen pembimbing'),
    ('proposal_kaprodi_no', 'Proposal tidak disetujui kaprodi'),
    ('proposal_approved', 'Proposal approved')
)


class Proposal(models.Model):
    mahasiswa = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    judul = models.CharField(
        help_text='Judul Proposal.',
        blank=False,
        null=False,
        max_length=512,
    )

    def __str__(self):
        return f'Proposal {self.mahasiswa}'


class Status(models.Model):
    proposal = models.ForeignKey(
        Proposal, on_delete=models.CASCADE
    )
    status = models.CharField(
        help_text='Status',
        choices=STATUS,
        max_length=100
    )
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.timestamp} - {self.get_status_display()}'