# Celery

## Flask and Celery

**环境准备**

```bash
$ git clone https://github.com/wxnacy/study
$ cd study/python/celerys/flask_demo
$ pip install -r requirements.txt
```

**启动 Flask**

```bash
$ python run.py
```

**启动 Celery**

```bash
$ celery worker -A run.celery -l info
```
