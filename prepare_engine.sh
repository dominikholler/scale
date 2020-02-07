#!/bin/bash

source auth.sh

engine=$1
SSH="ssh root@$engine -o StrictHostKeyChecking=no"
$SSH yum install -y $OVIRT_REPO
$SSH yum update -y
$SSH yum install -y ovirt-engine
$SSH -T "cat > /root/answerfile.txt" <<EOF
[environment:default]
OVESETUP_CONFIG/fqdn=str:$OVIRT_HOSTNAME
OVESETUP_CONFIG/adminPassword=str:$OVIRT_PASSWORD
EOF
$SSH engine-setup --accept-defaults --offline --config-append=/root/answerfile.txt
$SSH engine-config -s HostPackagesUpdateTimeInHours=0
sleep 10
ansible-playbook add_networks.yml