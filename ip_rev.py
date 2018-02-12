#!/usr/bin/env python
import sys
import dns.resolver

bl = [ 'babl.rbl.webiron.net', 'cabl.rbl.webiron.net', 'stabl.rbl.webiron.net', 'all.rbl.webiron.net', 'crawler.rbl.webiron.net', 'truncate.gbudb.net', 'dnsbl.sorbs.net', 'safe.dnsbl.sorbs.net', 'http.dnsbl.sorbs.net', 'socks.dnsbl.sorbs.net', 'misc.dnsbl.sorbs.net', 'smtp.dnsbl.sorbs.net', 'web.dnsbl.sorbs.net', 'new.spam.dnsbl.sorbs.net', 'recent.spam.dnsbl.sorbs.net', 'old.spam.dnsbl.sorbs.net', 'spam.dnsbl.sorbs.net', 'escalations.dnsbl.sorbs.net', 'block.dnsbl.sorbs.net', 'zombie.dnsbl.sorbs.net', 'dul.dnsbl.sorbs.net', 'noservers.dnsbl.sorbs.net', 'rhsbl.sorbs.net', 'badconf.rhsbl.sorbs.net', 'nomail.rhsbl.sorbs.net', 'sbl.spamhaus.org', 'xbl.spamhaus.org', 'pbl.spamhaus.org', 'sbl-xbl.spamhaus.org', 'zen.spamhaus.org', 'dnsrbl.org', 'bl.spamcop.net', 'noptr.spamrats.com', 'dyna.spamrats.com', 'spam.spamrats.com', 'auth.spamrats.com', 'bl.spamcannibal.org', 'ix.dnsbl.manitu.net', 'srnblack.surgate.net', 'all.s5h.net', 'rbl.megarbl.net', 'rbl.realtimeblacklist.com', 'b.barracudacentral.org', 'dnsbl.spfbl.net', 'ubl.unsubscore.com', '0spam.fusionzero.com' ]


def class_ip():
  ipaddr = sys.argv[1].replace('"', '')
  ip_class = []
  for c in ipaddr.split("."):
    ip_class.append(int(c))
  return ip_class


def rev_class(*ip_class):
  rev_ip = [ class_ip()[3], class_ip()[2], class_ip()[1], class_ip()[0] ]
  rip    = ".".join( str(x) for x in rev_ip)
  qlist = []
  for e in bl:
    qlist.append(rip + "." + e)
  return qlist


def query_bl(*qlist):
  for e in qlist:
    a = dns.resolver.query(e, 'A')
    for rdata in a:
      print(rdata.answer)

if __name__ == '__main__':
  query_bl()
