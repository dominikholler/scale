#!/bin/bash

source auth.sh
for i in $(seq 1 95) ; do
  ansible-playbook -e $(printf host_name=ovirt-host-%02d $i) create_host.yml &
  sleep 50
done

# kill -f create_host.yml