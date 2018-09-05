import unittest
from app.bot import getProjectConfig


class TestBot(unittest.TestCase):

    def setUp(self):
        self.config = """
        - project: test01
          account: bot01
          authKey: xxxx
        - project: test02
          account: bot02
          authKey: xxxx
        """

    def test_valid_config(self):
        res = getProjectConfig(self.config, 'test01')
        self.assertDictEqual(res,
                {'account': 'bot01', 'authKey': 'xxxx', 'project': 'test01'})

    def test_empty_config(self):
        res = getProjectConfig("""""", 'test01')
        self.assertDictEqual(res,
                {'account': 'bot01', 'authKey': 'xxxx', 'project': 'test01'})


if __name__ == '__main__':
    unittest.main()
