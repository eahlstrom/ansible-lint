import os
import unittest

from ansiblelint import Runner, RulesCollection


class TestTaskIncludes(unittest.TestCase):

    def setUp(self):
        rulesdir = os.path.join('lib', 'ansiblelint', 'rules')
        self.rules = RulesCollection([rulesdir])

    def test_block_included_tasks(self):
        filename = 'test/blockincludes.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_block_included_tasks_with_rescue_and_always(self):
        filename = 'test/blockincludes2.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_included_tasks(self):
        filename = 'test/taskincludes.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_include_tasks_2_4_style(self):
        filename = 'test/taskincludes_2_4_style.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_import_tasks_2_4_style(self):
        filename = 'test/taskimports.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_include_tasks_with_block_include(self):
        filename = 'test/include-in-block.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 3)

    def test_include_tasks_in_role(self):
        filename = 'test/include-import-tasks-in-role.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        self.assertEqual(len(runner.playbooks), 4)

    def test_include_tasks_2_7_style(self):
        filename = 'test/taskincludes_2_7_style.yml'
        runner = Runner(self.rules, filename, [], [], [])
        runner.run()
        playbooks = runner.playbooks
        self.assertEqual(len(playbooks), 3)

        (fname, _) = next(x for x in playbooks if x[1] == 'playbook')
        self.assertTrue(os.path.isfile(fname), "expected {} to exist".format(fname))

        for x in playbooks:
            if x[1] == 'tasks':
                self.assertTrue(os.path.isfile(x[0]), "expected {} to exist".format(x[0]))
