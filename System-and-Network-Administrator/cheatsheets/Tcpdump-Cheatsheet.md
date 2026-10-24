# Tcpdump Cheatsheet

| Purpose | Example |
|---|---|
| List interfaces, where supported | `tcpdump -D` |
| Capture on interface | `tcpdump -i eth0` |
| Numeric addresses/ports | `tcpdump -nn -i eth0` |
| Limit packet count | `tcpdump -c 20 -i eth0` |
| Filter host | `tcpdump -i eth0 host 192.0.2.10` |
| Filter port | `tcpdump -i eth0 port 53` |
| TCP or UDP | `tcpdump -i eth0 tcp` / `udp` |
| Write capture | `tcpdump -i eth0 -w capture.pcap` |
| Read capture | `tcpdump -nn -r capture.pcap` |
| Combine filters | `tcpdump -i eth0 'tcp and port 443'` |

Replace interface and example IP with verified lab values. Capture only authorized traffic; PCAP files may contain sensitive data.
Related note: [Tcpdump Commands](../04-Networking/01-Tcpdump-Commands.md)
