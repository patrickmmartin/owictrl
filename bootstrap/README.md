# Bootstrapping

This is a one-off on most debian machines which is quickly rectified

## Prerequisites

Currently the requirements are 
* libusb
* pyusb
* arm connected
* arm and batteries not flat

## Checking
run 
    
    ./check
    

sample output for a properly configured system is (output will vary in version)
   
    ...owictrl/bootstrap$ ./check 
    checking libusb versions
    ii  libgusb2                              0.1.3-5                            amd64        GLib wrapper around libusb1
    ii  libusb-0.1-4:amd64                    2:0.1.12-20+nmu1                   amd64        userspace USB programming library
    ii  libusb-0.1-4:i386                     2:0.1.12-20+nmu1                   i386         userspace USB programming library
    ii  libusb-1.0-0:amd64                    2:1.0.11-1                         amd64        userspace USB programming library
    ii  libusbmuxd1                           1.0.7-2                            amd64        USB multiplexor daemon for iPhone and iPod Touch devices - library
    checking for python-pip
    ii  python-pip                            1.1-3                              all          alternative Python package installer
    lsarms: 	find OWI Edge robot arms
    startup:	import prerequisites
    seek:   	find arm
    seek:   	complete
    seek:    	arm found
   

if there is nothing for libusb, pyusb then try

     
     sudo ./setup
     

You will need to OK any apt-get installation of libusb with Y

If all is well, you can then try 
   
    sudo ./armdemo.py 
   
in the ../utils dir and enjoy!
