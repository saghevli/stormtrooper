# datagen.py
# generates CSV .data file for input to svmachine.py
# Requires DPKT by Dug Song & Jon Oberheide, available here: code.google.com/p/dpkt/downloads/list

# run like:
# python datagen.py > filename.data

from __future__ import print_function
import dpkt
import socket
import sys
import pprint
#import whois

# def dnsLookup(dst_ip):
# 	try:
# 		# tuple = socket.gethostbyaddr(dst_ip)
# 		domain = whois.query(dst_ip)
# 		print(domain.__dict__)
# 		return domain.name
# 	except socket.herror:
# 		return "ERROR"

# def isBlocked(dst_ip):
# 	return dst_ip.find('74.125') >= 0 or dst_ip.find('173.194') >= 0
# 	# print(name)
# 	# #return False
# 	# # return name == 'ord08s08-in-f16.1e100.net'
# 	# if name == "ERROR" :
# 	# 	return False
# 	# return name.find('1e100.net') > 0


def main():
	filename = sys.argv[1]
	last_time = 0
	flows = {}
	for ts, pkt in dpkt.pcap.Reader(open(filename, 'r')):
		
		eth = dpkt.ethernet.Ethernet(pkt)
		if eth.type != dpkt.ethernet.ETH_TYPE_IP:
			continue
		ip = eth.data
	    
		dst_ip_addr_str = socket.inet_ntoa(ip.dst)
		if last_time == 0:
			delta = 0
		else:
			delta = ts - last_time

		last_time = ts

		packetList = [ ts, len(pkt), delta, dst_ip_addr_str ]

		# size, time delta, is dest IP blocked
		#if dst_ip_addr_str.find("192.168") < 0:
		#	print( len(pkt),",",delta,",",isBlocked(dst_ip_addr_str), sep='')

		# size, IAT, dest IP addr
		#print( len(pkt),",",delta,",",dst_ip_addr_str, sep='')

		ipkey = dst_ip_addr_str
		home = '192.168.'
		src_ip_addr_str = socket.inet_ntoa(ip.src)

		if ipkey.find(home) >= 0:
			ipkey = src_ip_addr_str

		if ipkey in flows:
			flows[ipkey].append(packetList)
		else:
			flows[ipkey] = [ packetList ]

	#pprint.pprint(flows)
        for key in flows:
            print(key, len(flows[key]))


if __name__ == "__main__":
    main()


