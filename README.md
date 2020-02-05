# scale
* create auth.sh
```
export DO_API_TOKEN=TODO
export OVIRT_HOSTNAME=ovirt.dyndns.org
export OVIRT_USERNAME=admin@internal
export OVIRT_PASSWORD=TODO
export ANSIBLE_HOST_KEY_CHECKING=False
```
* create Engine VM manually
* install Engine VM: `./prepare_engine.sh 167.71.61.xx`
* create hosts `./run_host_playbook.sh`
