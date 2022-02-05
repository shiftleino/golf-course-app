from invoke import task

# STARTING THE APP
@task
def start(ctx):
    ctx.run("flask run")

# FOR USING PYLINT
@task
def lint(ctx):
    ctx.run("pylint src")