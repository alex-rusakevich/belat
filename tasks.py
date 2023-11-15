from invoke import run, task


@task
def compile(context):
    run("python -m compileall .")


@task
def cbelat(context):
    run("python cbelat.py")


@task
def test(context):
    run("python -m pytest tests/")


@task
def testcov(context):
    run("python -m pytest tests/ --cov=belat")


@task
def cbelat(context):
    run("python cbelat.py")


@task
def req(context):
    run("pipenv install")
    run("pipenv install --dev")


@task(pre=(req, compile))
def install(context):
    ...
