from nose.tools import *
import subprocess
import os

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

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

def import_db(db_name, dump_file):
    run_command("createdb %s" % db_name)
    run_command("psql %s < %s" % (db_name, dump_file))

def test_basic():
    drop_db("hfa_events")
    tables = list_tables()
    assert("hfa_events" not in tables)
    import_db("hfa_events", "./assignment/data.pgdump")
    tables = list_tables()
    assert("hfa_events" in tables)
    count = run_command('psql -d hfa_events -c "select count(*) from events;"')
    assert("22" in count)

