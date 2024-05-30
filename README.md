# Django_Hopital

https://docs.google.com/document/d/1b3Cy2HGCNPf-fNsG8ojSIp7VDZZMZ_cp9wftFeABBY4/edit

```
url db: https://cloud.mongodb.com/
mail: minhtan.amela@gmail.com
password: 2V%/C2BzfpGM\*QC

password db: xDtwuHClFwnA5ENf

# Nếu mng không connect được mongo --> check ip đc add vào mongo chưa tại [đây](https://cloud.mongodb.com/v2/665821680d982749b330baba#/security/network/accessList)
```

```
# settings.py
DATABASES = {
    "default": {
        "ENGINE": "djongo",
        "NAME": "search_db",
        "ENFORCE_SCHEMA": False,
        "CLIENT": {
            "host": "mongodb+srv://minhtan: xDtwuHClFwnA5ENf@hopital.zz5pptw.mongodb.net/?retryWrites=true&w=majority&appName=hopital"
        },
    },
}
```

```
 pip install virtualenv

 python -m venv env

 source env/bin/activate

 pip install -r requirements.txt
```
