import scapy.all as scapy
import optparse


def get_user_input():
    parse_obj = optparse.OptionParser()
    parse_obj.add_option("-i", "--ipaddress", dest="ip_address", help="Enter IP address")
    (user_input, args) = parse_obj.parse_args()

    if not user_input.ip_address:
        print("Error!Enter IP address")

    return user_input


def scan_network(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")

    combined_packets = broadcast_packet / arp_request
    (answered, unanswered) = scapy.srp(combined_packets, timeout=1)
    answered.summary()


user_ip_address = get_user_input()
scan_network(user_ip_address.ip_address)
