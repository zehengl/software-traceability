class Dataset(object):
    @property
    def code(self):
        raise NotImplementedError

    @property
    def name(self):
        raise NotImplementedError

    @property
    def description(self):
        raise NotImplementedError


# fmt: off
class CM1(Dataset):
    code = "cm1"
    name = "CM1"
    description = "CM1 is a science instrument developed by NASA."


class CM1_Sub(Dataset):
    code = "cm1_sub"
    name = "CM1_Sub"
    description = "CM1_sub is a subset of CM1."


class GanttProject(Dataset):
    code = "gantt"
    name = "GanttProject"
    description = "GanttProject is a Java-based project management software."


class MODIS(Dataset):
    code = "modis"
    name = "MODIS"
    description = "MODIS is a software system developed by NASA."


class Pine(Dataset):
    code = "pine"
    name = "Pine"
    description = "Pine is a text-based email client developed by the University of Washington."


class WorldVistA(Dataset):
    code = "wvcchit"
    name = "WorldVistA"
    description = "WorldVistA is an electronic health information system developed by the USA Veterans Administration."
# fmt: on
