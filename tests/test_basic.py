import pytest
from odoo_find_runbot_instance import runbot_admin_user_credentials, runbot_unpriv_user_credentials


def test_pytest_fixture(runbot_url_db,
                        runbot_url_db_user_pwd,
                        runbot_url_db_user_pwd_unpriv):
    adm_cred = runbot_admin_user_credentials()
    assert len(adm_cred) == 2
    admin_user, admin_pwd = adm_cred
    assert isinstance(admin_user, str)
    assert isinstance(admin_pwd, str)
    assert len(admin_user) > 0
    assert len(admin_pwd) > 0
    
    unpriv_cred = runbot_unpriv_user_credentials()
    assert len(unpriv_cred) == 2
    unpriv_user, unpriv_pwd = unpriv_cred
    assert isinstance(unpriv_user, str)
    assert isinstance(unpriv_pwd, str)
    assert len(runbot_url_db) == 3

    assert len(runbot_url_db) == 3
    url, url_jsonrpc, db = runbot_url_db
    assert isinstance(url, str)
    assert len(url) >= 8
    assert isinstance(url_jsonrpc, str)
    assert url_jsonrpc.endswith('/jsonrpc')
    assert len(url_jsonrpc) >= 16
    assert isinstance(db, str)
    assert len(db) > 0

    assert len(runbot_url_db_user_pwd) == 5
    assert url == runbot_url_db_user_pwd[0]
    assert url_jsonrpc == runbot_url_db_user_pwd[1]
    assert db == runbot_url_db_user_pwd[2]
    assert admin_user == runbot_url_db_user_pwd[3]
    assert admin_pwd == runbot_url_db_user_pwd[4]

    assert len(runbot_url_db_user_pwd_unpriv) == 5
    assert url == runbot_url_db_user_pwd_unpriv[0]
    assert url_jsonrpc == runbot_url_db_user_pwd_unpriv[1]
    assert db == runbot_url_db_user_pwd_unpriv[2]
    assert unpriv_user == runbot_url_db_user_pwd_unpriv[3]
    assert unpriv_pwd == runbot_url_db_user_pwd_unpriv[4]
