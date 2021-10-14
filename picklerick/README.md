<div align="center">
Sep 29, 2021, Wednesday<br>
Notes by: Mayank Kumar Prajapati<br>
Machine Name: Pickle Rick<br>
URL:https://tryhackme.com/room/picklerick
</div>

***
This Rick and Morty themed challenge requires you to exploit a webserver to find 3 ingredients that will help Rick make his potion to transform himself back into a human from a pickle.
## Nmap Scan:
```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 1a:9c:2a:a3:08:30:18:66:63:ec:c1:fe:70:8f:92:42 (RSA)
|   256 48:d2:78:b6:30:81:69:da:0a:d9:e4:17:77:fc:ff:4b (ECDSA)
|_  256 c2:c5:87:3e:7c:c5:ba:c4:fc:4d:fa:db:db:86:e0:c5 (ED25519)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
| http-methods: 
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache/2.4.18 (Ubuntu)
|_http-title: Rick is sup4r cool
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

NSE: Script Post-scanning.
Initiating NSE at 11:47
Completed NSE at 11:47, 0.00s elapsed
Initiating NSE at 11:47
Completed NSE at 11:47, 0.00s elapsed
Initiating NSE at 11:47
Completed NSE at 11:47, 0.00s elapsed
Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.12 seconds
           Raw packets sent: 1123 (49.412KB) | Rcvd: 1053 (42.128KB
```

## Task 1:
1. What is the first ingredient Rick needs?
```

```
2. Whats the second ingredient Rick needs?
```
```

3. Whats the final ingredient Rick needs?
```

```
