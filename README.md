# django_sample

# 如何创建Django项目
``` 
conda create -n import-excel python=3.10.6
conda activate import-excel
pip install django
django-admin startproject django_sample
```

- 添加restframework、MySQL 、添加特定功能的独立模块
```
pip install djangorestframework
pip install mysqlclient
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'import_excel',
        'USER': 'root',
        'PASSWORD': 'root',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


python manage.py startapp app

INSTALLED_APPS [
...
'rest_framework',
'app',
]

```

 

- 添加 model (实体)
- 生成表
```
python manage.py makemigrations
python manage.py migrate
```



```
pip install pandas
pip install openpyxl
```


```
python manage.py createsuperuser
```
1030907690
1030907690@qq.com
123456



# 生成requirements.txt文件
```
pip install pipreqs
pipreqs . --encoding=utf-8
``` 


# 参考
- https://juejin.cn/post/7044953698350399502
- https://www.bilibili.com/video/BV1zi421S7dX/