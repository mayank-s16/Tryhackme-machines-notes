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
	old_file_name = new_file_name
	print(f"{new_file_name}")



