=============
Template Tags
=============

Pagination Tags
---------------

pagination
~~~~~~~~~~

Inclusion tag for "Digg Style" pagination. Uses template ``hort/pagination.html``.

arguments
.........

``object_list_view``

    Pattern or name of the list view you are paginating.

available settings
..................

``PAGINATION_RANGE``

    Number of pages to display before truncation. Defaults to 20.

``PAGINATION_TRAILING``

    Number of "trailing" pages to display before and after page list. Defaults to 2.

context
.......

``object_list_view``

    Pattern or name of the list view you are paginating.

``page_obj``

    Django page object for the current page.

``paginator``

    Django paginator object.

``page_range``

    Range representing the pages to display. If pages exceed ``PAGINATION_RANGE`` this might be truncated.

``pages_before``

    Pages before truncated ``page_range``.

``pages_after``

    Pages after truncated ``page_range``.

Sample usage::

    {% pagination "my_list_view_name" %}


UI Tags
-------

section
~~~~~~~

Takes a list and splits in into "sections". Useful for displaying grids of things.

arguments
.........

``list``

    The list you want to split up.

``by``

    The number of items you want in each section.

``as``

    The context variable you want to return the sectioned list as.

Say you have a list of names::

    names_list = ['Dustin', 'Sean', 'Steve', 'Eliana', 'Megan']

Sample usage::

    {% section names_list by 2 as sectioned_names_list %}
    {% for names_list in sectioned_names_list %}
    <ul>
        {% for name in names_list %}
        <li>{{ name }}</li>
        {% endfor %}
    </ul>
    {% endfor %}

This would produce::

    <ul>
        <li>Dustin</li>
        <li>Sean</li>
    </ul>
    <ul>
        <li>Steve</li>
        <li>Eliana</li>
    </ul>
    <ul>
        <li>Megan</li>
    </ul>

chunk
~~~~~

Takes a list and "chunks" it up. Useful for displaying columns of things.

arguments
.........

``list``

    The list you want to chunk.

``by``

    The number of items you want in each chunk.

``as``

    The context variable you want to return the chunked list as.

Say you have a list of names::

    names_list = ['Dustin', 'Sean', 'Steve', 'Eliana', 'Megan']

Sample usage::

    {% chunk names_list by 2 as chunked_names_list %}
    {% for names_list in chunked_names_list %}
    <ul>
        {% for name in names_list %}
        <li>{{ name }}</li>
        {% endfor %}
    </ul>
    {% endfor %}

This would produce::

    <ul>
        <li>Dustin</li>
        <li>Sean</li>
        <li>Steve</li>
    </ul>
    <ul>
        <li>Eliana</li>
        <li>Megan</li>
    </ul>
