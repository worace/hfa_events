import subprocess

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
    return run_command("psql %s < %s" % (db_name, dump_file))

if __name__ == "__main__":
    db_name = "hfa_events" #TODO: parameterize this by dev/prod/test
    import_file = "./assignment/data.pgdump"
    print drop_db(db_name)
    print import_db(db_name, import_file)
