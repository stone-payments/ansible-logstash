# Ansible Role: Logstash

An Ansible Role that installs Logstash on RedHat/CentOS Debian/Ubuntu.

This role is still configured only to work for Cerberus cluster.

## Requirements

Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables

Available variables are listed below, along with default values (see `defaults/main.yml`):

The port over which Logstash will listen for beats.

    logstash_elasticsearch_hosts:
      - http://localhost:9200

The hosts where Logstash should ship logs to Elasticsearch.

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

    logstash_input_files:
      - 01-input.conf

    logstash_output_files:
      - 03-output.conf.j2

    logstash_filter_files:
      - 02-filter.conf

Default configuration files.

## Other Notes
This role gives only the setup for a dedicated Logstash server and still has some hardcoded configurations regarding our Cerberus cluster. The use of this role on other configurations and Logstash as an agent is under development.

## Example Playbook

    - hosts: all
      roles:
        - buy4.java
        - buy4.logstash
      vars:
        logstash_enabled_on_boot: yes
        remove_java: false

## License

MIT / BSD

## To Do

  - Receives a dictionarie to be used on the inputs/filters/outpus configuration files.
  - Setup logstash as agent
