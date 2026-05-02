import pytest

params = {
    "+70000000011": "User with money on bank account",
    "+70000000022": "User without money on bank account",
    "+70000000033": "User with operations on bank account"
}


@pytest.mark.parametrize(
    "phone_number",
    params.keys(),
    ids=lambda nomer_telefona: f"{nomer_telefona}  {params[nomer_telefona]}"
)
def test_identifiers(phone_number: str):
    pass
