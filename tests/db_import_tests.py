from nose.tools import *
import app.db_import as db

def test_verifying_db_import():
    assert True
    db.drop_db("hfa_events")
    assert("hfa_events" not in db.list_tables())
    db.import_db("hfa_events", "./assignment/data.pgdump")
    assert("hfa_events" in db.list_tables())
    cmd = 'psql -d hfa_events -c "select count(*) from events;"'
    count = db.run_command(cmd)
    assert("22" in count)

