import pytest


from datasets import CM1, CM1_Sub, Dataset, GanttProject, MODIS, Pine, WorldVistA


@pytest.mark.parametrize("cls", [CM1, CM1_Sub, GanttProject, MODIS, Pine, WorldVistA])
def test_class_definition(cls):
    assert cls().code
    assert cls().name
    assert cls().description


@pytest.mark.parametrize("attr", ["name", "code", "description"])
def test_not_implemented_error(attr):
    with pytest.raises(NotImplementedError):

        class TestNotImplemented(Dataset):
            pass

        assert getattr(TestNotImplemented(), attr)
