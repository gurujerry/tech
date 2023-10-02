Telos Tech Club Class on Network Security

## Network Components
- Internet Protocol address (**IP address**)
  - Dynamic Host Configuration Protocol (**DHCP**)
- Common Ports
  - Domain Name System (**DNS**) `53`
  - Hypertext Transfer Protocol (**HTTP**) `80`
  - Hypertext Transfer Protocol Secure (**HTTPS**) `443`
  - Secure Shell (**SSH**) - `22`
  - Remote Desktop Protocol (**RDP**) - `3389`
- Accounts: User versus Administrator

### Network Topology
- Wide Area Network (**WAN**) vs Local Area Network (**LAN**) boundaries
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
- Password Attacks - used to access a computer
  - Dictionary
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
