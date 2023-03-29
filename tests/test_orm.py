from faudantic import FaunaModel, Field, q


class Mock(FaunaModel):
    name: str = Field(..., unique=True)
    age: int = Field(..., index=True)


def test_provision():
    assert Mock.provision() == None


def test_create_not_none():
    mock = Mock(name="John", age=20)
    obj = mock.create()
    assert obj is not None
    assert Mock.delete(obj.ref)


def test_create_name():
    mock = Mock(name="Oscar", age=33)
    obj = mock.create()
    assert obj.name == "Oscar"
    assert Mock.delete(obj.ref)


def test_create_age():
    mock = Mock(name="Pedro", age=44)
    obj = mock.create()
    assert obj.age == 44
    assert Mock.delete(obj.ref)


def test_create_ref_length():
    mock = Mock(name="Hermione", age=22)
    obj = mock.create()
    assert len(obj.ref) == 18
    assert Mock.delete(obj.ref)


def test_find():
    mock = Mock(name="Sinister1", age=33)
    obj = mock.create()
    obj2 = Mock.find(obj.ref)
    assert obj2.name == "Sinister1"
    assert Mock.delete(obj.ref)


def test_find_unique():
    mock = Mock(name="Sinister2", age=33)
    obj = mock.create()
    obj2 = Mock.find_unique("name", "Sinister2")
    assert obj2.name == "Sinister2"
    assert Mock.delete(obj.ref)


def test_find_many():
    mock = Mock(name="Sinister4", age=33)
    obj = mock.create()
    _generator = Mock.find_many("age", 33)
    items = [item for item in _generator]
    assert len(items) == 1
    assert items[0].name == "Sinister4"
    assert Mock.delete(obj.ref)


def test_find_all():
    for i in range(10):
        mock = Mock(name=f"mock{i}", age=33)
        mock.create()

    _generator = Mock.find_all()
    items = [item for item in _generator]
    assert len(items) == 10
    for i in range(10):
        assert Mock.delete(items[i].ref)


def test_update():
    mock = Mock(name="Siniestro666", age=33)
    obj = mock.create()
    Mock.update(ref=obj.ref, age=44)
    obj2 = Mock.find(obj.ref)
    assert obj2.age == 44
    assert Mock.delete(obj.ref)


def test_delete_collection():
    _q = Mock.q()
    _q(q.delete(q.collection("mock")))
    assert True