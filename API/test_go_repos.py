import unittest
import go_repos


class TestGoRepos(unittest.TestCase):

    def test_status_code(self):
        self.assertEqual(go_repos.r.status_code, 200)

    def test_num_repositories(self):
        self.assertTrue(go_repos.response_dict['total_count'] > 30000)


if __name__ == '__main__':
    unittest.main()
