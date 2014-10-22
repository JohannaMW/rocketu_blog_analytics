from fabric.colors import green, yellow
from fabric.api import *
from fabric.contrib.files import upload_template

env.hosts = ['54.169.70.170']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/blog_analytics.pem'
env.shell = "/bin/bash -l -i -c"

@task
def ubuntu_hello():
    with hide("stdout"):
        output = run("lsb_release -a")
        print(yellow(output))

@task
def hello():
    print(green("I'm alive!"))

@task
def create_file(file_name):
    local("touch ~/Desktop/{}.txt".format(file_name))

@task
def create_directory():
    local("mkdir ~/Desktop/my_directory")

@task
def create_dir(path, name):
    local("mkdir ~/{}/{}".format(path, name))

@task
def deploy():
    with prefix("workon blog_analytics"):
        with cd("/home/ubuntu/rocketu_blog_analytics"):
            run("git pull origin master")
            #run("pip install -r requirements.txt")
            run("./manage.py migrate")
            run("./manage.py collectstatic --noinput")
    restart_app()

def restart_app():
    sudo("service supervisor restart")
    sudo("service nginx restart")

@task
def setup_postgres(database_name, password):
    sudo("adduser {}".format(database_name))
    sudo("apt-get install postgresql postgresql-contrib libpq-dev")

    with settings(sudo_user='postgres'):
        sudo("createuser {}".format(database_name))
        sudo("createdb {}".format(database_name))
        alter_user_statement = "ALTER USER {} WITH PASSWORD '{}';".format(database_name, password)
        sudo('psql -c "{}"'.format(alter_user_statement))

@task
def setup_nginx(project_name, server_name):
    upload_template("./deploy/nginx.conf",
                    "/etc/nginx/sites-enabled/{}.conf".format(project_name),
                    {'server_name': server_name},
                    use_sudo=True,
                    backup=False)

    restart_app()

@task
def setup_gunicorn(project_name):

    upload_template("./deploy/gunicorn.conf",
                    "~/{}/gunicorn.conf.py".format(project_name),
                    {'project_name' : project_name},
                    use_sudo=True,
                    backup=False)
    restart_app()

@task
def setup_supervisor(project_name, virtualenv_name):
    upload_template("./deploy/supervisor.conf",
                    "/etc/supervisor/conf.d/{}.conf".format(project_name),
                    {'project_name' : project_name,
                     'virtualenv_name' : virtualenv_name},
                    use_sudo= True,
                    backup=False)
    restart_app()