

def test_logstash_installed_plugins(Ansible, Command):
    defaults = Ansible("include_vars", "./defaults/main.yml")["ansible_facts"]
    plugins = defaults['logstash_install_plugins']

    logstash_plugins = Command("/usr/share/logstash/bin/logstash-plugin list").stdout

    assert plugins[0] in logstash_plugins
