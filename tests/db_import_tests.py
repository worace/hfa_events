from nose.tools import *
import app.db_import as db

@nottest
def test_verifying_db_import():
    # Disabling this during dev to avoid the slowdown
    # TODO: figure out how to include this as a separate test group/suite/etc
    db.drop_db("hfa_events")
    assert("hfa_events" not in db.list_tables())
    db.create_db("hfa_events")
    db.import_db("hfa_events", "./assignment/data.pgdump")
    assert("hfa_events" in db.list_tables())
    cmd = 'psql -d hfa_events -c "select count(*) from events;"'
    count = db.run_command(cmd)
    assert("22" in count)

