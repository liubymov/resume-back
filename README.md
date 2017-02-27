Resume
===
This is backend mock for resume project.


Start
---
`docker-compose up` - this command will start server on localhost
machine and 8000 port. `ctrl+c` will stop the server.


URLs
---
http://127.0.0.1:8000/ - here you can find descriptions of all APIs

http://127.0.0.1:8000/admin/ - here you can find admin interface, 
default login/password: `admin`/`admin`. 
For example you can add about page here.

Auth
---
Add header:
```
"Authorization: JWT <your_token>"
```
Where token – it's token from `http://127.0.0.1:8000/api-token-auth/` api