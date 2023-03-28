# Faudantic

### A simple, versatile, easy to use Document Relational Mapper for FaunaDB

Faudantic is a simple, versatile, easy to use Document Relational Mapper for FaunaDB. It is built on top of the official FaunaDB driver and Pydantic library and provides a simple way to define your models and interact with your FaunaDB database.

## Installation

```bash

pip install faudantic

```

## Usage

### Defining your models

```python

from typing import Optional, List
from faudantic import FaunaModel, Field, q

class User(FaunaModel):
    name: str = Field(...)
    email: str = Field(...,unique=True)
    age: int = Field(...,index=True)
    gender: Optional[str] = Field(default='Not Specified',index=True)

```

### Creating a new user

```python

user = User(name='John Doe',email='john@doe.com',age=30)

instance = user.create()

print(instance.ref)

# '1234567890ABCDEFGH'

```

### Updating a user

```python

user = User.update(ref='1234567890ABCDEFGH',age=31)

# User(...)

print("Happy Birthday John!")

```

### Deleting a user

```python

result = User.delete(ref='1234567890ABCDEFGH')

# True

print("Goodbye John!")

```

## Examples

Comming soon
