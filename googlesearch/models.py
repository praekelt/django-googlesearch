from django.db import models

from options.models import Options

class GoogleSearchOptions(Options):
    __module__ = 'options.models'

    partner_id = models.CharField(
        max_length=128,
        help_text="Google custom search partner ID, i.e. partner-pub-324234324:dsfhk3dskf.",
        blank=True,
        null=True,
    )

    class Meta():
        verbose_name = "Google search options"
        verbose_name_plural = "Google search options"
