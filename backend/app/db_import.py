import subprocess
import os

def run_command(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)
    output = []
    for line in p.stdout.readlines():
        output.append(line)

    p.wait()
    return "\n".join(output)

def drop_db(db_name):
    return run_command("psql -c 'DROP DATABASE %s';" % db_name)

def list_tables():
    return run_command("psql -P pager=off -c '\l'")

def create_db(db_name):
    run_command("createdb %s" % db_name)

def import_db(db_name, dump_file):
    return run_command("psql %s < %s" % (db_name, dump_file))

def migrate(db_name, schema = "./app/schema.sql"):
    run_command("psql -d %s -f '%s'" % (db_name, schema))

def setup():
    drop_db("hfa_events_dev")
    drop_db("hfa_events_test")

    create_db("hfa_events_dev")
    create_db("hfa_events_test")

    print import_db("hfa_events_dev", os.environ["PG_DUMP_FILE"])

    migrate("hfa_events_dev")
    migrate("hfa_events_test")

if __name__ == "__main__":
    setup()
