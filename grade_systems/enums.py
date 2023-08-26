from django.db import models
from django.utils.translation import gettext_lazy as _

class BranchOption(models.TextChoices):
    MATHS = "matematik", _("Matematik")
    PHYSICAL = "fizik", _("Fizik")
    KIMYA = "kimya", _("Kimya")
    CHEMICAL = "biyoloji", _("Biyoloji")
    LITERATURE = "edebiyat", _("Edebiyat")
    ENGLISH = "ingilizce", _("İngilizce")
    HISTORY = "tarih", _("Tarih")
    GEOGRAPHY = "coğrafya", _("Coğrafya")
        