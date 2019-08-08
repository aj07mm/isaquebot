import unittest
from mock import patch


from lambda_isaquebot import get_reply


class IsaqueBotTestCase(unittest.TestCase):
    @patch("lambda_isaquebot.get_random")
    def test_get_reply_sergio(self, mock_get_random):
        mock_get_random.return_value = 1
        self.assertEqual(get_reply("sergio"), 'Vamo fuma droga na casa do Sergio')
    def test_get_reply_no_match(self):
        self.assertEqual(get_reply("asodknas"), None)


if __name__ == "__main__":
    unittest.main()
