stormtrooper
============

A machine learning approach to fingerprinting web traffic

Software stack from pcap to machine learning:

*1. traffic capture

    capture data on the wire, filter on local IP address, export/save as .pcap file

    - store pcap in data_collection/streams/pcaps 

    - use site_get.sh or site_get_multiple.sh for collection

*2. split TCP streams

    data_collection/streams/pcap_split.sh <input_pcap> <output_directory>

    - input_pcap: from step 1

    - output_directory: new directory name, will be created in data_collection/streams

    - operation: split pcap into a number of streams as separate pcap files

*3. sanity checking

    - data_collection/pcap_ips.py <stream dir> <number of files>

    - stream dir: directory of split stream pcaps from step 2

    - number of files: number of files created in step 2, +1

      *note: you can run this while step 2 is still running, just limit the number of files to the number that have thus far been processed

*4. format for ML

    -data_collection/formatter.py <stream_dir> <number of files> <whitelist[file/0]> <threshold packet count>

    - stream_dir: directory of split pcaps from step 2

    - number of files: number of files to process from directory (upper bounded, non inclusive, so add 1)

    - whitelist: file with lines of the form:

        <ip_prefix> <classification>

     will match all IPs that begin with the prefix with the specified class
     classification should be one word, with only the first letter capitalized:
     ex: Google, Baidu, Telex-google, Umich_EECS

     ensure that if this class has been used before, you use the same exact spelling 

*5. BLJL

    - run classifier: ./bljl <training_file> <test_file>

      files are of the form outputted by formatter.py
