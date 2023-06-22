<h1 align='center' style="font-size:5rem"><b>Stole IP & Store it for Limiting</b></h1>
<br>

<div align="center">

### This Project gets Client IP Per every GET request they send
### And Stores their IP for Limiting Them in The Future

</div>

<br>

# Main Page 

<img src="https://github.com/shervinbdndev/IPLimiter/blob/master/images/granted.png">

# You can Limit IP in Admin Panel

<img src="https://github.com/shervinbdndev/IPLimiter/blob/master/images/admin.png">

# Now the Client Side Access is Denied

<img src="https://github.com/shervinbdndev/IPLimiter/blob/master/images/denied.png">

<h1 align="left">Precedences & Features</h1>

- [x] Admin Panel
- [x] Database Created by Django ORM
- [x] Able To Manage Admin Panel
- [x] Able To Customize Admin Panel
- [x] Able To Create Super Users Such as Admin
- [x] Able To Use Any Type of SQL Databases (Current Database is Sqlite3)
- [x] Backend Security
- [ ] Beautiful UI for Front-end Side

<br>

<h2 align='center'><b>Language used in This Project</h2>
<img src="https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white"></img>
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"></img>
<img src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"></img>
<img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"></img>

<br>

<h2 align='center'><b>WorkSpace</h2>
<img src="https://img.shields.io/badge/Intel-Core_i5_10600K-0071C5?style=for-the-badge&logo=intel&logoColor=white"></img>
<img src="https://img.shields.io/badge/NVIDIA-RTX2060 OC-76B900?style=for-the-badge&logo=nvidia&logoColor=white"></img>
<img src="https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white"></img>
<img src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white"></img>
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"></img>
<img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white"></img>
<img src="https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white"></img>
<img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black"></img>

<br>

<h1 align='center'><b>Installation</b></h1>
<br>

# Download and Extract ```Ngrok``` here

[Download Ngrok](https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-windows-amd64.zip)

After this you have to get your ```NGROK``` token in their website
<br>
You can use the main website of NGROK to get your ```Auth Token```.
<br>
Or you can use this document instead.

## Open Ngrok's Website and Sign up
You can [Sign up](https://dashboard.ngrok.com/signup) or [Log in](https://dashboard.ngrok.com/login).

After these steps go to [this](https://dashboard.ngrok.com/get-started/your-authtoken) and copy your ```Auth Token```.

Close The Website and go to the ``` Directory ``` that you ``` downloaded ``` ``` NGROK ```.

First of all Open your ```CMD``` or ```Powershell``` set your token.

```
$ ngrok.exe config add-authtoken <token> 
```

Congratulations. Your all set
<br>
Just run the command bellow to use your ```NGROK Server```.

```
$ ngrok.exe http 8000
``` 

<br><br>

# Django Configurations
## Migrate Database
Just run the commands bellow
```
$ py manage.py makemigrations
$ py manage.py migrate
```

<br>

## Apply These Changes
Replace your ```Forwarding Link``` from your ```Ngrok Terminal``` in your ```settings.py``` file and change these two properties.

<img src="https://github.com/shervinbdndev/IPLimiter/blob/master/images/forwarding_link.png">

```python
ALLOWED_HOSTS = [
    '92ab-151-246-78-89.ngrok-free.app',
]
```

```python
CSRF_TRUSTED_ORIGINS = [
    'https://92ab-151-246-78-89.ngrok-free.app',
]
```

<br>

## Run Your Server
After these steps you have to run your server.
```
$ py manage.py runserver 8000
```

### Make Sure that your ```NGROK's http Port``` is the ```same``` with your ```Django runserver Port```.

<br>

## Open Forwarding Link

Just Open your Forwarding Link.
<br>
Thats it.