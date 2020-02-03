# scale
* source auth.sh
```
export OVIRT_HOSTNAME=TODO
export OVIRT_USERNAME=admin@internal
export OVIRT_PASSWORD=TODO
export DIGITALOCEAN_ACCESS_TOKEN=TODO
export ANSIBLE_HOST_KEY_CHECKING=False
```
* create Engine VM manually
* install Engine VM:
```
engine=167.172.96.xx
ssh root@$engine yum install -y https://resources.ovirt.org/pub/yum-repo/ovirt-release43.rpm`
ssh root@$engine yum install -y ovirt-engine
ssh root@$engine -T "cat > /root/answerfile.txt" <<EOF
[environment:default]
OVESETUP_CONFIG/fqdn=str:$OVIRT_HOSTNAME
OVESETUP_CONFIG/adminPassword=str:$OVIRT_PASSWORD
EOF
ssh root@$engine engine-setup --accept-defaults --offline --config-append=/root/answerfile.txt
```
* prepare Engine
    `ansible-playbook add_networks.yml`
* create hosts `/home/dominik/Documents/scripts/venv/bin/python /home/dominik/work/scale/create_hosts.py > hostlist`
* add hosts `xargs -P15 -L1 ansible-playbook < hostlist`
