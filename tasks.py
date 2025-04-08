from invoke import task

@task
def start(ctx):
     ctx.run("python src/pongcode.py")