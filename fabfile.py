from fabric.api import lcd, local, task


@task
def test():
    with lcd('src'):
        local('PYTHONPATH=. pytest')
