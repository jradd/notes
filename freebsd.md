# FreeBSD







## OpenSSH


```
ChallengeResponseAuthentication no         
X11Forwarding                   no        
UsePAM                          no 
VersionAddendum                 none    # prevents os fingerprinting
```








Here's an example /etc/fstab line for a standard swap partition:

###############################################################################
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/ada0p3             none            swap    sw              0       0
###############################################################################

Now here's the same thing with the swap automatically encrypted:

###############################################################################
# Device                Mountpoint      FStype  Options         Dump    Pass#
/dev/ada0p3.eli         none            swap    sw              0       0
###############################################################################

All you need to do is add ".eli" to the device name. A one-time key will be
generated and destroyed when swap is unmounted, so the swap contents should
be unrecoverable. I'll note that OpenBSD has encrypted swap by default since
2005 and seems to get along fine.









## Package Management





Foot
______  

[source]:         https://vez.mrsk.me/freebsd-defaults.txt
