from django.db import models

from preferences.models import Preferences

class GoogleSearchPreferences(Preferences):
    __module__ = 'preferences.models'

    partner_id = models.CharField(
        max_length=128,
        help_text="Google custom search partner ID, i.e. partner-pub-324234324:dsfhk3dskf.",
        blank=True,
        null=True,
    )

    class Meta():
        verbose_name = "Google search preferences"
        verbose_name_plural = "Google search preferences"
