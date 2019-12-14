import os
from datetime import datetime

Npath = r'E:/Python codes/FMS_Logs'

if not os.path.exists(Npath):
    os.makedirs(Npath)
today = datetime.now()
os.mkdir('E:/Python codes/FMS_Logs/'+today.strftime('%d%m%Y-%H_%M'))
