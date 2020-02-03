import socket
import time

import digitalocean


def ssh_running(hostname):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
    return sock.connect_ex((hostname, 22)) == 0


manager = digitalocean.Manager()
all_ssh_keys = manager.get_all_sshkeys()

host_tag = 'ovirt-host'

# digitalocean.Droplet.create_multiple seems to work only up to 10 dropletes
for i in range(0, 95):
    droplet_name= 'ovirt-43-host-{:02d}'.format(i)
    # print('creating ' + droplet_name)
    droplet = digitalocean.Droplet(name=droplet_name,
                                   region='fra1',
                                   image='centos-7-x64',
                                   size_slug='s-1vcpu-2gb',
                                   ipv6=True,
                                   private_networking=True,
                                   monitoring=True,
                                   ssh_keys=all_ssh_keys,
                                   tags=[host_tag]
                                   )
    try:
        droplet.create()
    except:
        pass

droplets = manager.get_all_droplets(tag_name=host_tag)

for droplet in droplets:
    while not droplet.ip_address:
        time.sleep(1)
        droplet.load()

    while not ssh_running(droplet.ip_address):
        time.sleep(1)

for droplet in droplets:
    print('-i {}, prepare_host.yml'.format(droplet.ip_address))

for droplet in droplets:
    print(
        '-e ovirt_host={} -e ovirt_address={} add_host.yml'.format(
            droplet.name, droplet.ip_address)
    )
