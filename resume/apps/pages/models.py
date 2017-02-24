from django.db import models
from django.utils.translation import ugettext_lazy as _


class Page(models.Model):
    slug = models.SlugField(_('URL'), db_index=True)
    title = models.CharField(_('title'), max_length=200)
    content = models.TextField(_('content'), blank=True)

    class Meta:
        verbose_name = _('page')
        verbose_name_plural = _('pages')
        ordering = ('slug',)

    def __str__(self):
        return "%s -- %s" % (self.slug, self.title)
