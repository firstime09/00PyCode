import datetime, glob
from fungsi import build_data

path_f = 'Forest2020/M_8_1/*.txt' #---- read folder
glob_f = glob.glob(path_f)
data = open(glob_f[1])


data1 = build_data(data)

def year_date():
    year_file = data1['DATE_ACQUIRED']
    date_file = data1['SCENE_CENTER_TIME']
    date_file2 = date_file [1:16]
    all = year_file+" "+date_file2
    parsing = datetime.strptime(all, '%Y-%m-%d %H:%M:%S.%f')
    return parsing

dt = year_date()
print dt