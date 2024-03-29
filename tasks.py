import os
from io import StringIO

from invoke import run, task


@task
def clear(context):
    os.system("rm -rf build/*.*")
    os.system("rm -rf dist/*.*")
    os.system("rm -f *.spec")


@task
def build(context, folder_mode=False):
    BELAT_VERSION = (
        open(os.path.join("belat", "VERSION.txt"), "r", encoding="utf8").read().strip()
    )

    run(
        f'pyinstaller \
--name=belat-v{BELAT_VERSION} \
--noconfirm {"--onefile" if not folder_mode else ""} --windowed \
--icon "./ui/icons/favicon.ico" \
--add-data "./belat;belat/" \
--add-data "./ui;ui/" \
--add-data "./cbelat.py;." \
"./belat.py"'
    )


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


@task
def designer(context):
    run("qt6-tools designer ui/belat.ui")


@task
def update_version_txt(context):
    BELAT_VERSION = (
        open(os.path.join("belat", "VERSION.txt"), "r", encoding="utf8").read().strip()
    )

    latest_commit_msg = StringIO()
    run("git log -1 --pretty=%B", out_stream=latest_commit_msg)
    latest_commit_msg = latest_commit_msg.getvalue().strip()

    major, minor, patch = (int(i) for i in BELAT_VERSION.split("."))

    if "#patch" in latest_commit_msg:
        patch += 1
    elif "#minor" in latest_commit_msg:
        patch = 0
        minor += 1
    elif "#major" in latest_commit_msg:
        patch, minor = 0, 0
        major += 1

    NEW_VER = ".".join([str(i) for i in (major, minor, patch)])

    if NEW_VER == BELAT_VERSION:
        print("No new version marker, skipping")
    else:
        open(os.path.join("belat", "VERSION.txt"), "w", encoding="utf8").write(NEW_VER)
        print(f"New version is {NEW_VER}")
        run(f'git add -A . && git commit -m "#bump to {NEW_VER}"')


@task(pre=(update_version_txt,))
def tag(context):
    """Auto add tag to git commit depending on belat version"""

    BELAT_VERSION = (
        open(os.path.join("belat", "VERSION.txt"), "r", encoding="utf8").read().strip()
    )

    latest_tag = StringIO()

    run("git describe --abbrev=0 --tags", out_stream=latest_tag)
    latest_tag = latest_tag.getvalue().strip()

    if f"v{BELAT_VERSION}" != latest_tag:
        run(f"git tag v{BELAT_VERSION}")
        run(f"git push --tags")
    else:
        print("No new version, skipping")
