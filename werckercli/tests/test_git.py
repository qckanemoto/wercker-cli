import os

from werckercli.tests import (
    DataSetTestCase,
    TestCase,
    VALID_GITHUB_SSH_URL,
    VALID_BITBUCKET_SSH_URL,
    VALID_HEROKU_SSH_URL,
)

from werckercli.git import (
    get_priority,
    get_remote_options,
    get_source_type,
    get_username,
    GITHUB_PATTERN,
    BITBUCKET_PATTERN,
    HEROKU_PATTERN,

    SOURCE_GITHUB,
    SOURCE_BITBUCKET,
    SOURCE_HEROKU
)


class GetPriorityTests(TestCase):
    BITBUCKET_URL = VALID_BITBUCKET_SSH_URL
    GITHUB_URL = VALID_GITHUB_SSH_URL
    HG_SSH_URL = "ssh://hg@bitbucket.org/pypy/pypy"
    HG_HTTPS_URL = "https://bitbucket.org/pypy/pypy"

    def test_priority_two(self):

        result = get_priority(self.BITBUCKET_URL, "origin")
        self.assertEqual(result, 2)

        result = get_priority(self.GITHUB_URL, "origin")
        self.assertEqual(result, 2)

    def test_priority_one(self):
        result = get_priority(self.BITBUCKET_URL, "some_upstream")
        self.assertEqual(result, 1)

        result = get_priority(self.GITHUB_URL, "some_upstream")
        self.assertEqual(result, 1)

        result = get_priority(
            self.GITHUB_URL,
            "origin",
            prio_remote="not_origin"
        )

        self.assertEqual(result, 1)

    def test_priority_zero(self):
        result = get_priority(self.HG_SSH_URL, "origin")
        self.assertEqual(result, 0)

        result = get_priority(self.HG_HTTPS_URL, "origin")
        self.assertEqual(result, 0)


class GetRemoteOptionsTests(DataSetTestCase):
    repo_name = "multiple-remotes"

    def test_get_remotes(self):

        folder = os.path.join(
            self.folder,
            self.repo_name,
            self.get_git_folder()
        )
        options = get_remote_options(folder)

        self.assertEqual(len(options), 2)


class GetSourceTypeTests(TestCase):

    def test_github(self):

        result = get_source_type(
            VALID_GITHUB_SSH_URL,
            GITHUB_PATTERN
        )

        self.assertEqual(result, SOURCE_GITHUB)

        self.assertEqual(
            get_source_type(VALID_BITBUCKET_SSH_URL, GITHUB_PATTERN),
            None
        )
        self.assertEqual(
            get_source_type(VALID_HEROKU_SSH_URL, GITHUB_PATTERN),
            None
        )

    def test_bitbucket(self):

        result = get_source_type(
            VALID_BITBUCKET_SSH_URL,
            BITBUCKET_PATTERN
        )

        self.assertEqual(result, SOURCE_BITBUCKET)

        self.assertEqual(
            get_source_type(VALID_GITHUB_SSH_URL, BITBUCKET_PATTERN),
            None
        )
        self.assertEqual(
            get_source_type(VALID_HEROKU_SSH_URL, BITBUCKET_PATTERN),
            None
        )

    def test_heroku(self):

        result = get_source_type(
            VALID_HEROKU_SSH_URL,
            HEROKU_PATTERN
        )

        self.assertEqual(result, SOURCE_HEROKU)

        self.assertEqual(
            get_source_type(VALID_BITBUCKET_SSH_URL, HEROKU_PATTERN),
            None
        )
        self.assertEqual(
            get_source_type(VALID_GITHUB_SSH_URL, HEROKU_PATTERN),
            None
        )


class GetUserNAmeTests(TestCase):

    def test_github(self):

        result = get_username(VALID_GITHUB_SSH_URL)
        self.assertEqual(result, "wercker")

    def test_bitbucket(self):
        result = get_username(VALID_BITBUCKET_SSH_URL)
        self.assertEqual(result, "postmodern")
# def get_username(url):
#     source = get_preferred_source_type(url)

#     if source == SOURCE_GITHUB:
#         match = re.match(GITHUB_PATTERN, url)
#         return match.groupdict()['name']
#     else:
#         match = re.match(BITBUCKET_PATTERN, url)
#         return match.groupdict()['name']
