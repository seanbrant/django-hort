===============
Database Fields
===============


``PostSaveImageField``
======================

.. class:: PostSaveImageField(upload_to=None, [height_field=None, width_field=None, max_length=100, **options])

Inherits all attributes and methods form :class:`ImageField`, but saves
the image after the ``model`` is saved. This requires the field to *always*
be ``null=True`` and ``blank=True``.

.. warning::

    This field saves the image using a  ``post_save`` signal and queryset ``update`` on the model. This
    will result in an extra database query for every save.
