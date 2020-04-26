from invoke import task

@task
def clean(c):
    for f in ("build", "dist", "nmcipher.egg-info"):
        print(f"removing contents of directory '{f}'...")
        c.run(f"rm -rf {f}")

@task(clean)
def build(c):
    c.run("python setup.py sdist bdist_wheel")

@task
def upload(c):
    c.run("python -m twine upload dist/*")

@task
def doctest(c):
    c.run("python -m doctest nmcipher/cli.py -v")
