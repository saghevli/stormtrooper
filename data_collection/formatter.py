

from __future__ import print_function
import dpkt
import socket
import sys
import pprint
import operator

# whitelist file is of the form:
# <ip prefix> <ip label>
def main():
    if len(sys.argv) < 5:
        print("Usage: formatter.py <stream_dir> <number of files> <whitelist[file/0]> <threshold packet count>")
        return
    directory_name = sys.argv[1]
    max_file = int(sys.argv[2])
    min_packets = int(sys.argv[4])
    flows = {}
    whitelist = []
    drop_file_count = 0
    drop_packet_count = 0

    #print(max_file)

    if sys.argv[3] != '0':
        f = open(sys.argv[3], 'r')
        for line in f:
            pair = line.split(' ')
            assert(len(pair) == 2)
            #whitelist contains ip prefix and label
            whitelist.append([pair[0].rstrip(), pair[1].rstrip()])

    num_traces = 0

    content = ""

    for i in range(0, max_file):
        last_time = 0
        packet_count = 0
        list_of_packetLists = []
        server_ip = ""
        server_name = "Default"
        for ts, pkt in dpkt.pcap.Reader(open(directory_name + "/stream-" + str(i) + ".pcap", 'r')):
            eth = dpkt.ethernet.Ethernet(pkt)
            if eth.type != dpkt.ethernet.ETH_TYPE_IP:
                drop_packet_count += 1
                continue
            ip = eth.data
            dst_ip_addr_str = socket.inet_ntoa(ip.dst)
            src_ip_addr_str = socket.inet_ntoa(ip.src)

            # if first packet in the file, set server_ip to the remote ip
            # and check that it isn't equal to an outlier. if so, skip file:
            if packet_count == 0:
                server_ip = dst_ip_addr_str if src_ip_addr_str.find("172.31") == 0 else src_ip_addr_str
                # loop through whitelist and drop files that don't match
                found = False
                for pair in whitelist:
                    if server_ip.find(pair[0]) == 0:
                        found = True
                        server_name = pair[1]
                        break
                # if this ip not found on whitelist, drop file
                if not found:
                    sys.stderr.write("Dropped: " + server_ip + '\n')
                    break

            packet_count += 1

            if last_time == 0:
                delta = 0
            else:
                delta = ts - last_time

            last_time = ts

            packetList = [ ts, len(pkt), delta, dst_ip_addr_str ]
            list_of_packetLists.append(packetList)

        # if file skipped or not enough packets, continue
        if packet_count == 0 or packet_count < min_packets:
            drop_file_count += 1
            continue

        num_traces += 1
        flows[i] = [packet_count, list_of_packetLists]
        #uncomment to include server ip above classification for debugging
        #print(server_ip)
        #if server_ip.find("141.212") == 0:
            #print("Baidu")
         #   content = content + "Telex\n"
        #else:
            #print("Google")
         #   content = content + "Baidu\n"
        # server name is set when server IP is identified on whitelist
        content = content + server_name + "\n"
        #print(packet_count)
        content = content + (str(packet_count) + "\n")
        for pl in list_of_packetLists:
            classification = ""
            if pl[3].find("35.2") == 0 :
                classification = "recv"
            else :
                classification = "send"
            #print(pl[1], pl[2], classification)
            content += (str(pl[1]) + " " + str(pl[2]) + " " + str(classification) + "\n")

    print(num_traces)
    print(content)

    sys.stderr.write("dropped packets: " + str(drop_packet_count)
        + " dropped files: " + str(drop_file_count))



if __name__ == "__main__":
    main()
