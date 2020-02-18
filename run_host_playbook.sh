#!/bin/bash

source auth.sh

DELAY=70

for i in $(seq 1 95) ; do
  ansible-playbook -e $(printf host_name=ovirt-host-%02d $i) create_host.yml || \
      ansible-playbook -e $(printf host_name=ovirt-host-%02d $i) create_host.yml &
  sleep $((i*4 < $DELAY ? i*4 : $DELAY))
done

# pkill -f create_host.yml