# django-endpoint

An end point to run Django services on.

## Installation

The application depends on python and python-pip. It is also recommended to
install and use a virutal environment.

```bash
sudo apt-get install python python-pip
```

## Usage

To start the service set the environment variables, install the package and run
the development server. After this the end point will be available at
`http://127.0.0.1:8000/`.

```bash
git clone https://github.com/marcbperez/django-endpoint
cd reportservice-flask
pip install .
python manage.py migrate
python manage.py runserver
```

Once the migrations have successfully been applied, create the administration
panel user and log in at `http://127.0.0.1:8000/admin`.

```bash
python manage.py createsuperuser
```

To add a service module, start by declaring it in settings.py. Also, include the
module's URL configuration in urls.py:

```python
INSTALLED_APPS = [
    ...
    'tasklist',
]
```

```python
urlpatterns = [
    ...
    url(r'^tasklist/', include('tasklist.urls')),
]
```

## Testing

To test each indidual service use `python manage.py test`. For example, if we
wanted to run the tests for the `tasklist` service:

```bash
python setup.py test tasklist
```

## Troubleshooting

The [issue tracker][issue-tracker] intends to manage and compile bugs,
enhancements, proposals and tasks. Reading through its material or reporting to
its contributors via the platform is strongly recommended.

## Contributing

This project adheres to [Semantic Versioning][semver] and to certain syntax
conventions defined in [.editorconfig][editorconfig]. To get a list of changes
refer to the [CHANGELOG][changelog]. Only branches prefixed by *feature-*,
*hotfix-*, or *release-* will be considered:

  - Fork the project.
  - Create your new branch: `git checkout -b feature-my-feature develop`
  - Commit your changes: `git commit -am 'Added my new feature.'`
  - Push the branch: `git push origin feature-my-feature`
  - Submit a pull request.

## Credits

This project is created by [marcbperez][author] and maintained by its
[author][author] and contributors.

## License

This project is licensed under the [Apache License Version 2.0][license].

[author]: https://marcbperez.github.io
[issue-tracker]: https://github.com/marcbperez/django-endpoint/issues
[editorconfig]: .editorconfig
[changelog]: CHANGELOG.md
[license]: LICENSE
[semver]: http://semver.org
