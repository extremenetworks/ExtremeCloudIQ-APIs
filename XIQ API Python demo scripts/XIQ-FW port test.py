#! /usr/bin/python

import telnetlib
import socket
import _thread
import requests

class PortTester(object):

    _thread_count = 0

    def __init__(self, input, log):

        for row in input:
            _thread.start_new(self.testPort, (row[0], row[1], log))
            self._thread_count = self._thread_count + 1
        while self._thread_count > 0:
            pass


    def testPort(self, host, port, log):
        #print 'Testing %s on port %s' % (host, port)
        try:
            connection = telnetlib.Telnet(host, port, 10)
            log.write('%s,%s,pass\n' % (host,port))
            log.flush()
            print('%s:%s pass' %(host, port))
        except:
            log.write('%s,%s,fail\n' % (host,port))
            log.flush()
            print('%s:%s fail' %(host, port))
        self._thread_count = self._thread_count - 1

def main():

    output = open('results.txt', 'w')
    default_pass = False
    fallback_pass = False

    print("\nExtreme Networks XIQ Reachbility test")
    print("(c) 2021 Extreme Networks.\n\n")

    print("Testing internet access (extremecloudiq.com:80)")
    PortTester([["Extremecloudiq.com","80"]], output)

    print ("\nTesting the ability to reach the ExtremeCloudIQ Global Data center.")
    XIQ_Default_Servers = [['redirector.aerohive.com', '22'], ['redirector.aerohive.com', '443'], ['hmupdates-ng.aerohive.com', '443'], ['extremecloudiq.com', '443'], ['cloud-rd.aerohive.com', '443']]
    PortTester(XIQ_Default_Servers, output)
    udpTestForXIQ('redirector.aerohive.com', 12222, output)

    print("\nTesting the ability to reach the ExtremeCloudIQ regional Data center")
    Update_Servers = [['nl-gcp.extremecloudiq.com', '443'], ['nl-gcp.extremecloudiq.com', '2083']]
    PortTester(Update_Servers, output)

    print("\nTesting license Server Communication")
    Update_Servers = [['hmupdates-ng.aerohive.com', '443']]
    PortTester(Update_Servers, output)


    print("\nTesting response time")
    timeXIQ= requests.get("https://extremecloudiq.com").elapsed.total_seconds()
    timeXIQ2= requests.get("https://nl-gcp.extremecloudiq.com").elapsed.total_seconds()
    timeXIQ3= requests.get("https://va2.extremecloudiq.com").elapsed.total_seconds()
    timeXIQ4= requests.get("https://redirector.aerohive.com").elapsed.total_seconds()
    timeXIQ5= requests.get("https://hmupdates-ng.aerohive.com").elapsed.total_seconds()

    print("https://extremecloudiq.com {}".format(timeXIQ))
    print("https://nl-gcp.extremecloudiq.com {}".format(timeXIQ2))
    print("https://va2.extremecloudiq.com {}".format(timeXIQ3))
    print("https://redirector.aerohive.com {}".format(timeXIQ4))
    print("https://hmupdates-ng.aerohive.com {}".format(timeXIQ5))

    print("\n\nTest complete.")

def udpTestForXIQ (host, port, log):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    except socket.error:
        print( 'Failed to create socket')

    #host = input[0] # first element in passed array.
    #port = input[1] # second element in passes array.
    message = "70408000000000000000012c040045000009f61900001f4000380000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
    hexMessage =bytes.fromhex(message)

    try:
        s.sendto(hexMessage, (host, port))
        # receive data from the client
        s.setblocking(0) # Set to non-blocking.
        s.settimeout(10) # give the server 10 seconds to respond.
        data = s.recvfrom(1024)
        reply = data[0]
        address = data[1]
        # write the result to the log
        log.write('%s,%s,pass\n' % (host,port))
        log.flush()
        print('%s:%s pass ' %(host, port, ))

    except socket.error as msg:
        print(host + ':' + str(port) + ' failed\nError code: ' + str(msg[0]) + '  Message: ' + msg[1])
        # write to the log
        log.write('%s,%s,fail\n' % (host,port))
        log.flush()


if __name__ == '__main__':
    main()
