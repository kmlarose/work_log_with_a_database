import unittest

import work_log


class EntryModelTests(unittest.TestCase):
    #def setUp(self):
        #work_log.initialize()

    def test_initialize(self):
        self.assertIn('entry', work_log.db.get_tables())
