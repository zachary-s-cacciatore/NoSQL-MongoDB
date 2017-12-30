import xlrd
from zipfile import ZipFile
datafile = "2013_ERCOT_Hourly_Load_Data.xls"


def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]

    coast_data = [sheet_data[r][1] for r in range(1, len(sheet_data))]
    
    exceltime = [sheet_data[r][0] for r in range(1, len(sheet_data))]
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(exceltime[coast_data.index(max(coast_data))], 0),
            'maxvalue': max(coast_data),
            'mintime': xlrd.xldate_as_tuple(exceltime[coast_data.index(min(coast_data))], 0),
            'minvalue': min(coast_data),
            'avgcoast': sum(coast_data)/float(len(coast_data))
    }
    
    
    return data


def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
