# Network Packet Capture with Tcpdump Cheatsheet

> **Operational Quick Reference for Network Administrators & Blue Team SOC Analysts**  
> Companion detailed notes: [01-Tcpdump-Commands.md](../04-Networking/01-Tcpdump-Commands.md)

---

## ⚡ Essential Command-Line Options

$$\text{Syntax:}\quad \mathbf{tcpdump}\quad [\mathbf{options}]\quad [\mathbf{BPF\ Filter\ Expression}]$$

| Flag | Meaning | Operational Purpose |
|:---:|---|---|
| **`-i <iface>`** | Interface | Specifies capture interface (e.g., `eth0`, `ens33`, `any` for all interfaces) |
| **`-D`** | List Devices | Displays all available network interfaces |
| **`-nn`** | Numeric Only | **CRITICAL:** Disables both IP (DNS) and port name resolution to prevent query loops |
| **`-c <N>`** | Packet Count | Automatically exits capture after receiving N packets |
| **`-w <file.pcap>`**| Write to PCAP | Saves raw binary packets to disk for Wireshark analysis |
| **`-r <file.pcap>`**| Read PCAP | Replays and analyzes an offline capture file |
| **`-v`, `-vv`** | Verbose | Displays IP Time-To-Live (TTL), identification numbers, and protocol headers |
| **`-X`** | Hex + ASCII | Prints packet payload in both Hexadecimal and ASCII text |
| **`-A`** | ASCII Only | Prints packet payload as readable text (ideal for HTTP, SMTP, DNS) |
| **`-s 0`** | Snapshot Length | Captures the entire packet payload without truncation (65535 bytes) |
| **`-e`** | Link-Layer | Displays Layer 2 MAC addresses |

---

## 🔍 Berkeley Packet Filter (BPF) Syntax

| BPF Filter Type | Syntax Primitives | Example Query |
|---|---|---|
| **Protocol** | `tcp`, `udp`, `icmp`, `arp`, `ip` | `tcpdump -nn -i eth0 icmp` |
| **Host IP** | `host <IP>` | `tcpdump -nn -i eth0 host 192.168.1.50` |
| **Direction** | `src`, `dst`, `src or dst` | `tcpdump -nn -i eth0 src host 10.0.0.1` |
| **Subnet (CIDR)** | `net <CIDR>` | `tcpdump -nn -i eth0 net 192.168.10.0/24` |
| **Single Port** | `port <num>` | `tcpdump -nn -i eth0 port 53` |
| **Port Range** | `portrange <start-end>` | `tcpdump -nn -i eth0 portrange 20-25` |
| **Boolean Logic** | `and` (`&&`), `or` (`\|\|`), `not` (`!`) | `tcpdump -nn -i eth0 'host 192.168.1.5 and not port 22'` |

---

## 🚩 TCP Control Flags Reference

$$\text{Format in Output:}\quad \mathbf{Flags\ [X]}$$

| Flag Symbol | TCP Flag Name | Meaning in Network State Machine |
|:---:|---|---|
| **`[S]`** | **SYN** | Connection initiation (Step 1 of 3-Way Handshake) |
| **`[S.]`** | **SYN-ACK** | Connection acknowledged by server (Step 2 of Handshake; dot `.` = ACK) |
| **`[.]`** | **ACK** | Connection established (Step 3), or general data acknowledgment |
| **`[P]`** or **`[P.]`** | **PSH** (Push) | Sender requests receiver to push buffered data immediately to app |
| **`[F]`** or **`[F.]`** | **FIN** | Sender requests clean, graceful connection termination |
| **`[R]`** | **RST** (Reset) | **Connection Refused** (Port closed) or abrupt session termination |

---

## 🚀 High-Frequency Administrator One-Liners

```bash
# 1. Capture web traffic (HTTP or HTTPS) to a specific server:
tcpdump -nn -i eth0 'host 192.168.1.50 and (port 80 or port 443)'

# 2. Capture all traffic EXCEPT your own SSH management session:
tcpdump -nn -i eth0 'not port 22'

# 3. Monitor live DNS queries sent to domain controller:
tcpdump -nn -i eth0 -A 'dst host 192.168.1.2 and port 53'

# 4. Save 1,000 packets of suspicious traffic to PCAP for Wireshark analysis:
tcpdump -nn -i eth0 -w incident.pcap -c 1000 'host 10.0.0.99'

# 5. Read an offline PCAP file and display only packets with RST flag:
tcpdump -nn -r incident.pcap 'tcp[tcpflags] & tcp-rst != 0'

# 6. Detect SYN flood attack (pure SYN packets without ACK):
tcpdump -nn -i eth0 'tcp[tcpflags] & tcp-syn != 0 and tcp[tcpflags] & tcp-ack == 0'
```
