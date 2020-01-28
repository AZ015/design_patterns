from Behavioral.observer.push_observer import DataSource, SpreadSheet, Chart

if __name__ == '__main__':
    data_source = DataSource()
    sheet_1 = SpreadSheet()
    sheet_2 = SpreadSheet()
    chart = Chart()

    data_source.add_observer(sheet_1)
    data_source.add_observer(sheet_2)
    data_source.add_observer(chart)
    data_source.value = 1
