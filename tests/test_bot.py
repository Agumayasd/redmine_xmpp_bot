import unittest
import os
import yaml
from app.bot import getProjectConfig, openConfigFile, EmptyConfigFile


class TestBot(unittest.TestCase):

    def createConfigFile(self, path, data):
        f = open(path, 'w')
        f.write(data)
        f.close()

    def setUp(self):
        self.config = """
        - project: test01
          account: bot01
          authKey: xxxx
        - project: test02
          account: bot02
          authKey: xxxx
        """
        self.configFile = '/tmp/config.yaml'

    def tearDown(self):
        if os.path.exists(self.configFile):
            os.remove(self.configFile)

    def test_open_valid_config(self):
        self.createConfigFile(self.configFile, self.config)
        res = openConfigFile(self.configFile)
        self.assertEqual(len(res), 2)

    def test_file_does_not_exist(self):
        with self.assertRaises(FileNotFoundError):
            openConfigFile(self.configFile)

    def test_empty_file(self):
        self.createConfigFile(self.configFile, "")
        with self.assertRaises(EmptyConfigFile):
            openConfigFile(self.configFile)

    def test_open_invalid_config(self):
        invalidConfig = """
        - project: name
        null
        """
        self.createConfigFile(self.configFile, invalidConfig)
        with self.assertRaises(yaml.YAMLError):
            openConfigFile(self.configFile)


    # def test_valid_config(self):
    #     res = getProjectConfig(self.config, 'test01')
    #     self.assertDictEqual(res,
    #             {'account': 'bot01', 'authKey': 'xxxx', 'project': 'test01'})

    # def test_empty_config(self):
    #     res = getProjectConfig("""""", 'test01')
    #     self.assertDictEqual(res,
    #             {'account': 'bot01', 'authKey': 'xxxx', 'project': 'test01'})


if __name__ == '__main__':
    unittest.main()
