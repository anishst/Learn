import time
import sys
from tqdm import tqdm

# using tqdm lib - https://github.com/tqdm/tqdm
for i in tqdm(range(0, 8000001)):
    i = i+2


#  using custom function
def progress(count, total, status=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))

    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)

    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', status))
    sys.stdout.flush()


total = 400
i = 0
while i < total:
    progress(i, total, status='Doing very long job')
    time.sleep(0.5)  # emulating long-playing job
    i += 1