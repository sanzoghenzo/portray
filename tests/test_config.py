from hypothesis_auto import auto_test

from portray import config


def test_repository_properties():
    auto_test(config.repository)


def test_repository_custom_config(project_dir):
    assert config.repository(project_dir) == {
        "edit_uri": "edit/master/",
        "repo_name": "portray",
        "repo_url": "https://github.com/timothycrosley/portray",
    }

    assert config.repository(project_dir, repo_name="different_name") == {
        "edit_uri": "edit/master/",
        "repo_name": "different_name",
        "repo_url": "https://github.com/timothycrosley/portray",
    }

    assert config.repository(project_dir, edit_uri="edit/develop/") == {
        "edit_uri": "edit/develop/",
        "repo_name": "portray",
        "repo_url": "https://github.com/timothycrosley/portray",
    }

    assert config.repository(
        project_dir, repo_url="https://github.com/timothycrosley/examples"
    ) == {
        "edit_uri": "edit/master/",
        "repo_name": "examples",
        "repo_url": "https://github.com/timothycrosley/examples",
    }

    assert config.repository(
        project_dir, repo_url="https://bitbucket.org/atlassian/stash-example-plugin.git"
    ) == {
        "edit_uri": "src/default/docs/",
        "repo_name": "stash-example-plugin",
        "repo_url": "https://bitbucket.org/atlassian/stash-example-plugin",
    }

    assert config.repository(
        project_dir, repo_url="git@bitbucket.org:atlassian/stash-example-plugin.git"
    ) == {
        "edit_uri": "src/default/docs/",
        "repo_name": "stash-example-plugin",
        "repo_url": "https://bitbucket.org/atlassian/stash-example-plugin",
    }

    assert config.repository(project_dir, repo_url="not_actually_a_valid_url") == {
        "repo_name": "not_actually_a_valid_url",
        "repo_url": "not_actually_a_valid_url",
    }


def test_repository_no_config_no_repository(temporary_dir):
    assert config.repository(temporary_dir) == {}