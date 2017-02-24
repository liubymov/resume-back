from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Resume(models.Model):
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)
    created_at = models.DateTimeField(_('created at'), auto_now_add=True)
    author = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        verbose_name = _('resume')
        verbose_name_plural = _('resumes')
        ordering = ('-created_at',)

    def __str__(self):
        return "%s - %s (%s)" % (self.author, self.title, self.created_at)
