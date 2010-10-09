from django.db import models

from hort.db.fields import PostSaveImageField


def album_upload_to(instance, filename):
    return 'album-%s.jpg' % instance.pk


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover = PostSaveImageField(upload_to=album_upload_to)
