from fabric.api import local, task


@task
def test(*args):
    local('pip install -e .')

    params_str = ' '.join(args)
    local('pytest {}'.format(params_str))


@task
def build():
    local('python setup.py sdist')
