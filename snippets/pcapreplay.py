#!/usr/bin/env python
import argparse
from scapy.all import *

def send_packet(recvd_pkt, src_ip, dst_ip, count):
  """ Send modified packets """
  pkt_cnt = 0
  p_out = []

  for p in recvd_pkt:
    pkt_cnt += 1
    new_pkt = p.payload
    new_pkt[IP].dst = dst_ip
    new_pkt[IP].src = src_ip
    del new_pkt[IP].chksum
    p_out.append(new_pkt)
    if pkt_cnt % count == 0:
      send(PacketList(p_out))
      p_out = []

  send(PacketList(p_out))
  print("Total packets sent: %d" % pkt_cnt)

  if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Sniff Packets')
  parser.add_argument('--infile', action="store", dest="infile", default='test_pcap.pcap')
  parser.add_argument('--src-ip', action="store", dest="src_ip", default='8.8.8.8')
  parser.add_argument('--dst-ip', action="store", dest="dst_ip", default='104.236.56.13')
  parser.add_argument('--count', action="store", dest="count", default=100, type=int)
  given_args = ga = parser.parse_args()
  global src_ip, dst_ip
  infile, src_ip, dst_ip, count = ga.infile,
  ga.src_ip, ga.dst_ip, ga_count
  try:
    pkt_reader = PcapReader(infile)
    send_packet(pkt_reader, src_ip, dst_ip, count)
  except IOError:
    print("Failed reading %s contents" % infile)
    sys.exit(1)
