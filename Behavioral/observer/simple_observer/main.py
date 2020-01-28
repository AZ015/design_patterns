from Behavioral.observer.simple_observer.chart import Chart
from Behavioral.observer.simple_observer.data_source import DataSource
from Behavioral.observer.simple_observer.spread_sheet import SpreadSheet

if __name__ == '__main__':
    data_source = DataSource()
    sheet_1 = SpreadSheet()
    sheet_2 = SpreadSheet()
    chart = Chart()

    data_source.add_observer(sheet_1)
    data_source.add_observer(sheet_2)
    data_source.add_observer(chart)
    data_source.value = 1
