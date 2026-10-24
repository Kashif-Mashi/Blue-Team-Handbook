# Tcpdump Network Packet Capture Cheatsheet

> **Operational Quick Reference**  
> **Parent Foundational Guide:** [01-Tcpdump-Commands.md](../04-Networking/01-Tcpdump-Commands.md) | [Cheatsheets Index](README.md)

---

## ⚙️ Essential Command Options

| Command / Option | Purpose | Example | Important Note |
|---|---|---|---|
| `tcpdump -D` | List interfaces | `tcpdump -D` | [Read-Only] Shows all available capture interfaces and indices. |
| `-i <interface>` | Select interface | `tcpdump -i eth0` | [Read-Only] Specify network interface. Use `-i any` for all active NICs. |
| `-n` | No IP resolution | `tcpdump -i eth0 -n` | [Performance] Disables reverse DNS lookups to prevent network lag. |
| `-nn` | No IP or port resolution | `tcpdump -i eth0 -nn` | [Performance] Prints raw IP and numerical port numbers (`80`, `22`). |
| `-c <count>` | Packet limit | `tcpdump -i eth0 -c 100` | [Capture Control] Exits automatically after capturing `<count>` packets. |
| `-v` / `-vv` / `-vvv`| Verbosity | `tcpdump -i eth0 -vv` | [Display] Increases packet header decoding detail (TTL, IP ID, flags). |
| `-A` | ASCII payload | `tcpdump -i eth0 -A port 80` | [Inspection] Prints payload in readable ASCII (ideal for HTTP, SMTP). |
| `-X` | Hex and ASCII | `tcpdump -i eth0 -X port 53` | [Inspection] Dumps payload in side-by-side hex and ASCII columns. |
| `-w <file.pcap>` | Write to PCAP | `tcpdump -i eth0 -w dump.pcap`| [Storage] Captures raw binary frames to disk for Wireshark analysis. |
| `-r <file.pcap>` | Read from PCAP | `tcpdump -r dump.pcap -nn` | [Read-Only] Parses and analyzes packets from saved file offline. |
| `-s 0` | Full snapshot length | `tcpdump -i eth0 -s 0 -w cap.pcap`| [Capture Control] Captures full 65535-byte frame without truncation. |
| `-e` | Link-layer header | `tcpdump -i eth0 -e` | [Inspection] Prints source and destination Ethernet MAC addresses. |

---

## 🎯 Berkeley Packet Filter (BPF) Primitives

| BPF Primitive | Purpose | Example Syntax | Operational Context |
|---|---|---|---|
| `host <IP>` | Filter single host | `tcpdump -i eth0 -nn host 192.168.1.50` | Matches if specified IP is source OR destination. |
| `src host <IP>` | Filter source IP | `tcpdump -i eth0 -nn src host 10.0.0.5` | Matches packets originating from this host. |
| `dst host <IP>` | Filter destination IP | `tcpdump -i eth0 -nn dst host 10.0.0.1` | Matches packets destined to this target. |
| `net <CIDR>` | Filter entire subnet | `tcpdump -i eth0 -nn net 192.168.1.0/24` | Captures all traffic across local or remote subnet. |
| `port <port>` | Filter port number | `tcpdump -i eth0 -nn port 80` | Matches TCP or UDP traffic on specific port. |
| `src port <port>` | Filter source port | `tcpdump -i eth0 -nn src port 53` | Captures DNS server responses. |
| `dst port <port>` | Filter dest port | `tcpdump -i eth0 -nn dst port 443` | Captures outbound HTTPS connection attempts. |
| `portrange <start-end>`| Filter port range | `tcpdump -i eth0 -nn portrange 20-25` | Matches multiple consecutive ports. |
| `icmp` | Filter ICMP protocol | `tcpdump -i eth0 -nn icmp` | Captures ping requests, replies, and unreachable notices. |
| `arp` | Filter ARP protocol | `tcpdump -i eth0 -nn arp` | Captures Address Resolution Protocol broadcasts/replies. |

---

## 🔗 Combining Filters with Logical Operators

Logical operators: **`and`** (`&&`), **`or`** (`||`), **`not`** (`!`).

| Target Traffic Scenario | BPF Command Example |
|---|---|
| **Exclude SSH Traffic (Avoid terminal loop)** | `tcpdump -i eth0 -nn not port 22` |
| **Inspect Web Traffic (HTTP and HTTPS)** | `tcpdump -i eth0 -nn "port 80 or port 443"` |
| **Specific Host and Port** | `tcpdump -i eth0 -nn host 192.168.1.100 and port 80` |
| **Outbound DNS Queries Only** | `tcpdump -i eth0 -nn src host 192.168.1.10 and udp dst port 53` |
| **Capture All Traffic Except Specific Subnet** | `tcpdump -i eth0 -nn not net 10.0.0.0/8` |

---

## 🛡️ TCP Control Flag Analysis

| TCP Flag Check | BPF Syntax | Detection Purpose |
|---|---|---|
| **TCP SYN Packets (New Connections)** | `tcpdump -i eth0 -nn "tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0"` | Identifies inbound connection attempts and SYN port scanning. |
| **TCP RST Packets (Connection Resets)** | `tcpdump -i eth0 -nn "tcp[tcpflags] & tcp-rst != 0"` | Detects rejected connections, port closures, or firewall resets. |
| **TCP FIN Packets (Graceful Termination)**| `tcpdump -i eth0 -nn "tcp[tcpflags] & tcp-fin != 0"` | Monitors connection teardown sequences. |

---

## ⚡ Field One-Liners for Emergency Triage

```bash
# 1. Quick sanity check: see who is talking on the wire without DNS lag
tcpdump -i eth0 -nn -c 20

# 2. Sniff plaintext web credentials (POST data) on port 80
tcpdump -i eth0 -nn -A -s 0 port 80

# 3. Capture 500 packets to file for Wireshark inspection
tcpdump -i eth0 -nn -s 0 -c 500 -w /tmp/incident.pcap

# 4. Read an existing PCAP file filtered for IP 10.0.0.15
tcpdump -r /tmp/incident.pcap -nn host 10.0.0.15
```
