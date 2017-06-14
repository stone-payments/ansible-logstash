# Ansible Role: Logstash

An Ansible Role that installs Logstash on RedHat/CentOS Debian/Ubuntu.

This role is still configured only to work for Cerberus cluster.

## Requirements

Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

    logstash_ssl_dir: /etc/pki/logstash
    logstash_ssl_certificate_file: logstash-forwarder-example.crt
    logstash_ssl_key_file: logstash-forwarder-example.key

Local paths to the SSL certificate and key files, which will be copied into the `logstash_ssl_dir`.

For utmost security, you should use your own valid certificate and keyfile, and update the `logstash_ssl_*` variables in your playbook to use your certificate.

To generate a self-signed certificate/key pair, you can use use the command:

    $ sudo openssl req -x509 -batch -nodes -days 3650 -newkey rsa:2048 -keyout logstash.key -out logstash.crt

Note that filebeat and logstash may not work correctly with self-signed certificates unless you also have the full chain of trust (including the Certificate Authority for your self-signed cert) added on your server. See: https://github.com/elastic/logstash/issues/4926#issuecomment-203936891

    logstash_enabled_on_boot: yes

Set this to `no` if you don't want logstash to run on system startup.

    logstash_install_plugins:
      - logstash-input-beats

A list of Logstash plugins that should be installed.

    logstash_config_dir: "/etc/logstash/conf.d"
    logstash_user: logstash
    logstash_group: logstash

The defaults for logstash confs location and permissions.

    force_pipeline_update: true
    downloaded_repos_temp_dir: "/tmp/downloaded_repos"

A flag to tell ansible whether it should update the custom pipelines and the default path where the role will download those pipelines.

## Example Playbook

    - hosts: all
      roles:
        - buy4.java
        - buy4.logstash
      vars:
        logstash_enabled_on_boot: yes
        remove_java: false

Additionally you can define a list of dicts containing the path to a git repository where are located the pipelines you should use. Each dict should have the repository path and the path to the directory where the pipeline files are located.

    - name: logstash service with pipeline
      hosts: group1
      roles:
        - buy4.java
        - buy4.logstash
      vars:
        logstash_enabled_on_boot: yes
        remove_java: false
        pipeline_repository:
          - {url: "your_repository_path", path: "path/to/the/directory/where/are/the/pipeline/files"}

## License

MIT / BSD

## To Do
  - Setup logstash as agent