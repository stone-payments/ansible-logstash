# Stone Payments - Logstash
This Ansible Role that installs Logstash on RedHat/CentOS

## Requirements
Though other methods are possible, this role is made to work with Elasticsearch as a backend for storing log messages.

## Role Variables
Available variables are listed below, along with default values (see [`defaults/main.yml`](defaults/main.yml)):

```yaml
logstash_pipeline_update: true
logstash_pipeline_repositories:
	- repo: git@github.com:stone-payments/logstash-pipelines.git
		path:
			- example-pipeline-path
```

Local paths to the SSL certificate and key files, which will be copied into the `logstash_ssl_path`.

For utmost security, you should use your own valid certificate and keyfile, and update the `logstash_ssl_*` variables in your playbook to use your certificate.

Note that filebeat and logstash may not work correctly with self-signed certificates unless you also have the full chain of trust (including the Certificate Authority for your self-signed cert) added on your server. See: https://github.com/elastic/logstash/issues/4926#issuecomment-203936891.

A list of Logstash plugins that should be installed:

```yaml
logstash_install_plugins:
	- logstash-input-beats
```

The defaults for logstash confs location and permissions:

```yaml
logstash_path_config: "/etc/logstash/conf.d"
logstash_user: logstash
logstash_group: logstash
```

A flag to tell ansible whether it should update the custom pipelines and the default path where the role will download those pipelines:

```yaml
logstash_pipeline_update: true
logstash_pipeline_repos_temp_dir: /tmp/logstash_pipeline_repos
```
## Example Playbook

```yaml
- hosts: all
	roles:
    - stone-payments.java
    - stone-payments.logstash
```

Additionally you can define a list of dicts containing the path to a git repository where are located the pipelines you should use. Each dict should have the repository path and the path to the directory where the pipeline files are located.

```yaml
- name: logstash service with pipeline
	hosts: all
    vars:
    logstash_ssl: true
    logstash_pipeline_update: true
    logstash_pipeline_repositories:
			- repo: "your_repository_path"
				path:
					- "path/to/the/directory/where/are/the/pipeline/files"
    roles:
    	- stone-payments.java
      - stone-payments.logstash
```

## Testing
This role implements unit tests with [Molecule](https://molecule.readthedocs.io/) on Docker. Notice that we only support Molecule 2.0 or greater. You can install molecule with:

```bash
pip install molecule
```

After having Molecule setup, you can run the tests with:
```bash
molecule test
```

## Contributing
Just open a PR. We love PRs!

## License
MIT
