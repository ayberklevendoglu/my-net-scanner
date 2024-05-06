import scapy.all as scapy

arp_request = scapy.ARP(pdst="10.0.2.1/24")
#scapy.ls(scapy.ARP())