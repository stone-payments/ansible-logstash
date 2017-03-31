import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('all')


def test_logstash_is_installed(Package):
    logstash = Package("logstash")
    assert logstash.is_installed


def test_logstash_is_running_and_enabled(Service):
    logstash = Service("logstash")
    assert logstash.is_running
    assert logstash.is_enabled
