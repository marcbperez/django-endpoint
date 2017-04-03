django-endpoint
===============

An end point to run Django services on.

Installation
------------

Start by downloading and building the project when necessary. The
following commands will do the job on most Debian based Linux
distributions.

.. code:: bash

    git clone https://github.com/marcbperez/django-endpoint
    cd django-endpoint
    sudo ./gradlew

Usage
-----

The installation process will install the project dependencies and
migrations. An administration user will also be created from the Gradle
build scripts parameters. Run the command below and login at
``http://127.0.0.1:8000/admin``.

.. code:: bash

    sudo python manage.py runserver

To add a service module, start by declaring it in ``settings.py`` and
include the module's URL configuration in ``urls.py``.

.. code:: python

    INSTALLED_APPS = [
        ...
        'myservice',
    ]

.. code:: python

    urlpatterns = [
        ...
        url(r'^myservice/', include('myservice.urls')),
    ]

Testing
-------

Test checks are executed automatically every time the project is built.
Builds can be done remotely or continuously on a development context.
For continuous integration and development use docker-compose. This is
recommended to keep the system clean while the project is built every
time the sources change.

.. code:: bash

    sudo docker-compose up

For continuous integration and development without any dependencies use
the Gradle wrapper. This is the best option if the wrapper is available
and the Docker context is not valid. For a full list of tasks, see
``sudo ./gradlew tasks --all``. For a CI cycle use
``sudo ./gradlew --continuous``.

For continuous integration and development without Docker or the project
wrapper use Gradle directly. This will create the wrapper in case it is
not present. Similar to the above, for a CI cycle use
``sudo gradle --continuous``. Gradle 3.4.1 is required for this to work.
Plain Docker is also available for remote integration tasks and alike.
Build the image with ``sudo docker build .`` and run a new container
with it. Information on how to install Docker and docker-compose can be
found in their `official
page <https://docs.docker.com/compose/install/>`__. A similar
installation guide is available `for
Gradle <https://gradle.org/install>`__.

Troubleshooting
---------------

The `issue tracker <https://github.com/marcbperez/django-endpoint/issues>`__
intends to manage and compile bugs, enhancements, proposals and tasks.
Reading through its material or reporting to its contributors via the
platform is strongly recommended.

Contributing
------------

This project adheres to `Semantic Versioning <http://semver.org>`__ and
to certain syntax conventions defined in
`.editorconfig <.editorconfig>`__. To get a list of changes refer to the
`CHANGELOG <CHANGELOG.md>`__. Only branches prefixed by *feature-*,
*hotfix-*, or *release-* will be considered:

-  Fork the project.
-  Create your new branch:
   ``git checkout -b feature-my-feature develop``
-  Commit your changes: ``git commit -am 'Added my new feature.'``
-  Push the branch: ``git push origin feature-my-feature``
-  Submit a pull request.

Credits
-------

This project is created by `marcbperez <https://marcbperez.github.io>`__ and
maintained by its `author <https://marcbperez.github.io>`__ and contributors.

License
-------

This project is licensed under the `Apache License Version
2.0 <LICENSE>`__.
