 <div align = "center"> _22-Sep-2021, Wednesday

  Notes by: Mayank Kumar Prajapati

  Machine Name: Vulnversity
  
  URL: https://tryhackme.com/room/vulnversity_
</div>

**Phase1: Reconnaissance**
***
> nmap -sV 10.10.227.240`

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

 **Phase2:  Locating directories using GoBuster**
 ***
> apt install gobuster\
> gobuster dir -u http://10.10.227.240:3333/ -w /usr/share/wordlists/dirbusterdirectory-list-2.3-medium.txt\
> gobuster dir -u http://10.10.227.240:3333/internal -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt

 What is the directory that has an upload form page?
/internal/

 Phase3: Compromise the webserver

Try upload a few file types to the server, what common extension seems to be blocked?
.php


 What is the name of the user who manages the webserver?
bill

 What is the user flag?
FInd it inside bill's home directory.



**Phase4: Privilege Escalation**
***
In Linux, SUID (set owner userId upon execution) is a special type of file permission given to a file. 
SUID gives temporary permissions to a user to run the program/file with the permission of the file owner (rather than the user who runs it).
For example, the binary file to change your password has the SUID bit set on it (/usr/bin/passwd).
This is because to change your password, it will need to write to the shadowers file that you do not have access to, root does, so it has root privileges to make the right changes.\
On the system, search for all SUID files. What file stands out?
/bin/systemctl
