def test_base(client):
    r = client.get('/')

    assert r.status_code == 200