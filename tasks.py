from invoke import task

# STARTING THE APP
@task
def start(ctx):
    ctx.run("flask run")