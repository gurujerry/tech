Telos Tech Club Class on Network Security

## Network Components
- **MAC address** (Media Access Control address) 
- **IP address** (Internet Protocol address)
- **DHCP** (Dynamic Host Configuration Protocol)
- Common Ports
  - **DNS** (Domain Name System) `53`
  - **HTTP** (Hypertext Transfer Protocol) `80`
  - **HTTPS** (Hypertext Transfer Protocol Secure) `443`
  - **SSH** (Secure Shell) - `22`
  - **RDP** (Remote Desktop Protocol) - `3389`
- Accounts: User versus Administrator

### Network Topology
- **WAN** (Wide Area Network) vs **LAN** (Local Area Network) boundaries
- Hardware
  - Routers/Modems
  - Firewalls (Hardware vs Software)
  - Switches

## Hacking
- What is OK to hack?
- Types of hackers
  - **Black hat** - accesses systems illegally, with malicious intent, and often for personal gain
  - **White hat** - has permission of the network owner, accesses legally and ethically. Example: penetration tester paid and authorized to conduct a security audit
  - **Gray hat** - may sometimes violate laws or usual ethical standards, but they do not have the malicious intent typical of a black hat hacker

### Types of attacks
- DNS Hijacking: [example](./example1_dns/)
- Password Attacks - used to access a computer
  - Dictionary: [example](./example2_dictionary/)
  - Brute Force
- Denial of Service (DOS) and Distributed (DDOS) - used to deny access a computer

### Payloads - what a hacker will install
Malware (Malicious Software)
- Virus: May delete files and attempt to infect other computers on network
- Ransomware: Makes files on computer inaccessible until a ransom is paid and files unlocked
- Crypto mining: Turns infected computer into a crypto miner
- Botnet

### Tools
- Kali Linux - an OS with a lot of hacking tools already loaded
  - `chntpw` : reset local Windows passwords
  - `aircrack-ng` : crack WiFi passwords
  - `nmap` : scan for network devices and computers
- Metasploit

### Prevention
- HoneyPot (give a demo)
- Logging
- Password attempts and backoffs

## More advanced?
- Bug / Exploit

## Demonstration ideas
Show how computers store an encrypted password
  - Linux `/etc/shadow` file
  - Encode a password: `echo password | md5sum`

## Interactive ideas
Packet Youtube video

## Launch a Python container
```bash
docker run -it --rm python:3.9.5 bash
pip3 install paramiko

```
