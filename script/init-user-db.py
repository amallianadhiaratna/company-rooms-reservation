import os
import subprocess


DATABASE_NAME= os.environ.get('DATABASE_NAME')
DATABASE_USER= os.environ.get('DATABASE_USER')
DATABASE_PASSWORD= os.environ.get('DATABASE_PASSWORD')
DATABASE_HOST= os.environ.get('DATABASE_HOST')
DATABASE_PORT= os.environ.get('DATABASE_PORT')
DATABASE_ROOT_PASSWORD= os.environ.get('DATABASE_ROOT_PASSWORD')

command = f"mysql -h {DATABASE_HOST} -p {DATABASE_PORT} -u root --password={DATABASE_ROOT_PASSWORD} < init-script.sql".split()
process = subprocess.Popen(command, stdout=subprocess.PIPE)
process.communicate()