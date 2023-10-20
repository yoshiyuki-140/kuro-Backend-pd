# The way to generate SECRET_KEY on your laptop.

## Generate SECRET_KEY
You have to move into project root Dir, In this case, you move to CivicSeek. And type the following code.

```bash
$ python3 manage.py shell
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'xxxx' <- This is generated secret key. 
```

# Example
```bash
> python3 manage.py shell
Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from django.core.management.utils import get_random_secret_key
>>> get_random_secret_key()
'_fr91ikc^!6!pu$0-1$*ivqhm!#7d72-3!b)a53#3a5qo$-+=q'
```

