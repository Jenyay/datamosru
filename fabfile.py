from fabric.api import local, task


@task
def test():
    local('pip install -e .')
    local('pytest')


@task
def build():
    local('python setup.py sdist')
