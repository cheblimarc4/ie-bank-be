from iebank_api.models import Account
import pytest


def test_create_account():
    """
    GIVEN a Account model
    WHEN a new Account is created
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "Spain", "€")
    assert account.name == "John Doe"
    assert account.country == "Spain"
    assert account.currency == "€"
    assert account.account_number != None
    assert account.balance == 0.0
    assert account.status == "Active"


def test_create_account_with_balance():
    """
    GIVEN a Account model
    WHEN a new Account is created with a balance
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "Spain", "€")
    account.balance = 100.0

    assert account.name == "John Doe"
    assert account.country == "Spain"
    assert account.currency == "€"
    assert account.account_number != None
    assert account.balance == 100.0
    assert account.status == "Active"


def test_edit_account():
    """
    GIVEN a Account model
    WHEN a new Account is created and edited
    THEN check the name, account_number, balance, currency, status and created_at fields are defined correctly
    """
    account = Account("John Doe", "Spain", "€")
    account.balance = 100.0

    assert account.name == "John Doe"
    assert account.country == "Spain"
    assert account.currency == "€"
    assert account.account_number != None
    assert account.balance == 100.0
    assert account.status == "Active"

    account.name = "Jane Doe"
    account.country = "France"
    account.currency = "$"
    account.balance = 200.0
    account.status = "Inactive"

    assert account.name == "Jane Doe"
    assert account.country == "France"
    assert account.currency == "$"
    assert account.account_number != None
    assert account.balance == 200.0
    assert account.status == "Inactive"