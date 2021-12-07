from sample import mod
from unittest import mock

class TestMod(object):

    @mock.patch("requests.get")
    def test_mod(self, mock_requests):
        mock_requests.return_value = {}
        assert mod.mod() == {}
