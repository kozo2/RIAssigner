from RIAssigner.data import PandasData


class PandasDataBuilder:

    def __init__(self):
        self._filename = None
        self._rt_unit = 'seconds'
        self._filetype = 'csv'

    def with_filename(self, filename: str):
        self._filename = filename
        return self

    def with_rt_unit(self, rt_unit: str):
        self._rt_unit = rt_unit
        return self

    def with_filetype(self, filetype: str):
        self._filetype = filetype
        return self

    def build(self) -> PandasData:
        data = PandasData(self._filename, self._filetype, self._rt_unit)
        return data
