## django-i5

This package enables quick and easy configuration for Django applications running behind [i5](https://github.com/nathan-osman/i5).

### Installation

```
pip install django-i5
```

### Usage

In your settings.py file, add the following:

```python
from django_i5 import *
```

The settings defined in the module will cover 99% of what you need to start your Django project. You will also need to define the following variable:

```python
ROOT_URLCONF = '[project].urls'
```
