from Behavioral.observer.pull_observer.chart import Chart
from Behavioral.observer.pull_observer.data_source import DataSource
from Behavioral.observer.pull_observer.spread_sheet import SpreadSheet

if __name__ == '__main__':
    data_source = DataSource()
    sheet_1 = SpreadSheet(data_source)
    sheet_2 = SpreadSheet(data_source)
    chart = Chart(data_source)

    data_source.add_observer(sheet_1)
    data_source.add_observer(sheet_2)
    data_source.add_observer(chart)
    data_source.value = 1
