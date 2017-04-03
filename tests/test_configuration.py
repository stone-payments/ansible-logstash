

def test_logstash_config_dir_present(File):
    logstash_config_dir = File("/etc/logstash/conf.d")
    assert logstash_config_dir.exists
    assert logstash_config_dir.is_directory
    assert logstash_config_dir.user == 'logstash'
    assert logstash_config_dir.group == 'logstash'
    assert logstash_config_dir.mode == 0755


def test_logstash_input_present(File):
    logstash_input = File("/etc/logstash/conf.d/01-input.conf")
    assert logstash_input.exists
    assert logstash_input.user == 'logstash'
    assert logstash_input.group == 'logstash'
    assert logstash_input.mode == 0644


def test_logstash_filter_present(File):
    logstash_input = File("/etc/logstash/conf.d/02-filter.conf")
    assert logstash_input.exists
    assert logstash_input.user == 'logstash'
    assert logstash_input.group == 'logstash'
    assert logstash_input.mode == 0644


def test_logstash_output_present(File):
    logstash_input = File("/etc/logstash/conf.d/03-output.conf")
    assert logstash_input.exists
    assert logstash_input.user == 'logstash'
    assert logstash_input.group == 'logstash'
    assert logstash_input.mode == 0644


def test_logstash_input_does_not_contains_file(File):
    logstash_input = File("/etc/logstash/conf.d/01-input.conf")
    logstash_input_content = logstash_input.content_string
    assert "file{\n" not in logstash_input_content
    assert "file {\n" not in logstash_input_content
