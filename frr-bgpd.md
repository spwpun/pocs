# Step to reproduce for frr-v8.3.0:
1. Using docker pull the latest frr image, and run a container with it. 
- https://hub.docker.com/layers/frr/frrouting/frr/v8.3.0/images/sha256-4d1343030d2e1f48aa61860b85485a8245cb21ce70fff9187c05011bfaa7b296
Then we can start bgpd daemon with container busybox terminal:
- `/usr/lib/frr/bgpd -f /etc/frr/bgpd.conf`
2. Then run poc.py with `python3 poc.py`, we can see the bgpd daemon has crashed.
```
2022/07/22 02:16:06 BGP: No backtrace available on this platform.
2022/07/22 02:16:06 BGP: lib/stream.c:417: stream_getw(): assertion (0) failed
BGP: Received signal 6 at 1658456166 (si_addr 0x6400000064, PC 0x7fef9beef3f1); aborting...
BGP: in thread bgp_process_packet scheduled from bgpd/bgp_io.c:269 bgp_process_reads()
core_handler: showing active allocations in memory group libfrr
core_handler: memstats:  Buffer                        :      2 *         24
core_handler: memstats:  Host config                   :      8 * (variably sized)
core_handler: memstats:  Command Argument Name         :   2052 * (variably sized)
core_handler: memstats:  Command Token Help            :   8731 * (variably sized)
core_handler: memstats:  Command Token Text            :   8731 * (variably sized)
core_handler: memstats:  Command Tokens                :  12061 *         72
core_handler: memstats:  RCU thread                    :      2 *        128
core_handler: memstats:  POSIX sync primitives         :      4 * (variably sized)
core_handler: memstats:  FRR POSIX Thread              :      4 * (variably sized)
core_handler: memstats:  Graph Node                    :  14243 *         32
core_handler: memstats:  Graph                         :     40 *          8
core_handler: memstats:  Hash Index                    :    287 * (variably sized)
core_handler: memstats:  Hash Bucket                   :   2344 *         32
core_handler: memstats:  Hash                          :    573 * (variably sized)
core_handler: memstats:  Connected                     :      1 *         48
core_handler: memstats:  Interface                     :      2 *        272
core_handler: memstats:  Link Node                     :    338 *         24
core_handler: memstats:  Link List                     :     43 *         40
core_handler: memstats:  Bitfield memory               :      2 * (variably sized)
core_handler: memstats:  Temporary memory              :     15 * (variably sized)
core_handler: memstats:  Nexthop                       :      1 *        144
core_handler: memstats:  Northbound Configuration      :      2 *         16
core_handler: memstats:  Northbound Node               :    240 *       1192
core_handler: memstats:  Prefix                        :      1 *         56
core_handler: memstats:  Privilege information         :      3 * (variably sized)
core_handler: memstats:  Ring buffer                   :      6 * (variably sized)
core_handler: memstats:  Skiplist Counters             :      2 *         68
core_handler: memstats:  Skip Node                     :      2 *        160
core_handler: memstats:  Skip List                     :      2 *         56
core_handler: memstats:  Socket union                  :      2 *        112
core_handler: memstats:  Stream FIFO                   :      6 *         64
core_handler: memstats:  Stream                        :     13 * (variably sized)
core_handler: memstats:  Route table                   :    100 *         56
core_handler: memstats:  Thread stats                  :     18 *         96
core_handler: memstats:  Thread Poll Info              :      6 *    8388608
core_handler: memstats:  Thread master                 :     12 * (variably sized)
core_handler: memstats:  Thread                        :     14 *        160
2022/07/22 02:16:06 BGP: [NJ2F2-2W769] 172.17.0.1 [Event] BGP connection closed fd 20
core_handler: memstats:  Typed-heap array              :      1 *        576
core_handler: memstats:  Typed-hash bucket             :      6 * (variably sized)
core_handler: memstats:  Vector index                  :  28567 * (variably sized)
core_handler: memstats:  Vector                        :  28567 *         24
core_handler: memstats:  VRF bit-map                   :      3 *          8
core_handler: memstats:  VRF                           :      1 *        216
core_handler: memstats:  VTY server                    :      3 *         32
core_handler: memstats:  Work queue name string        :      3 * (variably sized)
core_handler: memstats:  Work queue                    :      3 *        152
core_handler: memstats:  YANG module                   :      5 *         48
core_handler: memstats:  Redistribution instance IDs   :      6 *          2
core_handler: memstats:  Zclient                       :      2 *       3144
core_handler: memstats:  log thread-local buffer       :      2 *      24608
core_handler: showing active allocations in memory group logging subsystem
core_handler: memstats:  log file name                 :      1 *         14
core_handler: memstats:  log file target               :      2 *         80
core_handler: showing active allocations in memory group bgpd
core_handler: memstats:  Mac Hash Entry Intf String    :      2 * (variably sized)
core_handler: memstats:  Mac Hash Entry                :      2 *         16
core_handler: memstats:  BGP EVPN MH Information       :      1 *         56
core_handler: memstats:  BGP own address               :      1 *         64
core_handler: memstats:  BGP nexthop                   :      2 *        184
core_handler: memstats:  community-list handler        :      1 *        120
core_handler: memstats:  BGP synchronise               :     63 *         72
core_handler: memstats:  BGP static                    :      1 *        144
core_handler: memstats:  BGP connected                 :      1 *          4
core_handler: memstats:  BGP route                     :      1 *        112
core_handler: memstats:  BGP node                      :      3 *        192
core_handler: memstats:  BGP table                     :     87 *         56
core_handler: memstats:  BGP aspath str                :      1 *          1
core_handler: memstats:  BGP aspath                    :      1 *         40
core_handler: memstats:  BGP attribute                 :      1 *        304
core_handler: memstats:  BGP peer af                   :      2 *         80
core_handler: memstats:  BGP peer hostname             :      4 * (variably sized)
core_handler: memstats:  BGP peer                      :      3 *     733664
core_handler: memstats:  BGP listen socket details     :      2 *        144
core_handler: memstats:  BGP instance                  :      2 * (variably sized)
core_handler: memstats:  BGP Martian Addr Intf String  :      1 *          5
core_handler: memstats:  BGP PBR Context               :      1 *         32
core_handler: memstats:  BGP EVPN instance information :      1 *         56
core_handler: showing active allocations in memory group rfapi
core_handler: memstats:  RFAPI Import Table            :      1 *        208
core_handler: memstats:  RFAPI Generic                 :      1 *        296
core_handler: memstats:  NVE Configuration             :      1 *       2984
Aborted (core dumped)
```
3. And if you test it with frr git version a9b4458f6107af926df2c7ba20d0fd873bf6e99e, compile it with `-g` argument, you will see the backtrace which indicate the assert error is in `peek_for_as4_capability` function.
