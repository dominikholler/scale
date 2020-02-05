# scale
* create auth.sh
```
export DO_API_TOKEN=TODO
export OVIRT_HOSTNAME=TODO
export OVIRT_USERNAME=admin@internal
export OVIRT_PASSWORD=TODO
export ANSIBLE_HOST_KEY_CHECKING=False
export OVIRT_REPO=https://resources.ovirt.org/pub/yum-repo/ovirt-release43-snapshot.rpm
```
* create Engine VM manually
* ensure that $OVIRT_HOSTNAME maps to Engine VM
* install Engine VM: `./prepare_engine.sh 167.71.61.xx`
* create hosts `./run_host_playbook.sh`
