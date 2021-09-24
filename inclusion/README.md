<div align = "center">
Sep 24, 2021, Friday<br>
Notes by: Mayank Kumar Prajapati<br>
Machine Name: Inclusion<br>
URL: https://tryhackme.com/room/inclusion
</div>

***
Nmap Scan
```
# Nmap 7.91 scan initiated Fri Sep 24 02:47:44 2021 as: nmap -sV -sC -oN nmapScan 10.10.71.11
Nmap scan report for 10.10.71.11
Host is up (0.43s latency).
Not shown: 998 closed ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 e6:3a:2e:37:2b:35:fb:47:ca:90:30:d2:14:1c:6c:50 (RSA)
|   256 73:1d:17:93:80:31:4f:8a:d5:71:cb:ba:70:63:38:04 (ECDSA)
|_  256 d3:52:31:e8:78:1b:a6:84:db:9b:23:86:f0:1f:31:2a (ED25519)
80/tcp open  http    Werkzeug httpd 0.16.0 (Python 3.6.9)
|_http-server-header: Werkzeug/0.16.0 Python/3.6.9
|_http-title: My blog
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Fri Sep 24 02:48:10 2021 -- 1 IP address (1 host up) scanned in 26.19 seconds

```
**Task 1: Root it.**
---
1. User Flag.
```
*******
```
Website shows that LFI could be there.<br>
Found one page on website while normally browsing it. Injected directory traversal in `name` parameter, was able to see the user in /etc/passwd file with plain text username and password.

2. Root flag
```
*******
```
> sudo -l

```Matching Defaults entries for falconfeast on inclusion:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User falconfeast may run the following commands on inclusion:
    (root) NOPASSWD: /usr/bin/socat
```
Cick [here](https://gtfobins.github.io/gtfobins/socat/#sudo) to know how to perform privilege escalation with sudo privileges on `/usr/bin/socat`.

