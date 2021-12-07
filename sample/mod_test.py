from sample import mod
from unittest.mock import Mock, patch

class TestMod(object):

    @patch("requests.get")
    def test_mod(self, mock_requests):
        mock_response = Mock(status_code=200)
        mock_requests.return_value = mock_response
        assert mod.mod().status_code == 200
