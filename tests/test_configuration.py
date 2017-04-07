import yaml
repo_defined = False


with open('playbook.yml', 'r') as playbook_file:
    playbook_yaml = yaml.load(playbook_file)
    global repo_defined
    repo_defined = 'pipeline_repository' in playbook_yaml[0]['vars']


def test_logstash_config_dir_present(File):
    logstash_config_dir = File("/etc/logstash/conf.d")
    assert logstash_config_dir.exists
    assert logstash_config_dir.is_directory
    assert logstash_config_dir.user == 'logstash'
    assert logstash_config_dir.group == 'logstash'
    assert logstash_config_dir.mode == 0755


if repo_defined:
    def test_logstash_config_dir_not_empty(Command):
        cmd_ls = Command("ls -l /etc/logstash/conf.d")
        stdout = cmd_ls.stdout.strip('\n')
        assert len(stdout) >= 1
else:
    def test_logstash_config_dir_empty(Command):
        cmd_ls = Command("ls -l /etc/logstash/conf.d")
        stdout = cmd_ls.stdout.strip('\n')
        assert len(stdout) == 0
