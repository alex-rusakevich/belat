import os

from invoke import run, task

BELAT_VERSION = (
    open(os.path.join("belat", "VERSION.txt"), "r", encoding="utf8").read().strip()
)

os.environ["BELAT_BASE_DIR"] = ".belat"


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


@task
def designer(context):
    run("qt6-tools designer ui/belat.ui")


@task
def tag(context):
    """Auto add tag to git commit depending on belat version"""
    run(f"git tag v{BELAT_VERSION}")
    run(f"git push --tags")
