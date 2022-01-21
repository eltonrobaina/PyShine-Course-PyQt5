import datetime

formats=["%d/%m/%Y %H:%M:%S",
        "%d/%m/%Y %H:%M%f",
        "%Y-%m-%d %H:%M:%S.%f",
        "%m/%d/%Y",
        "%d/%m/%Y",
        "%m-%d-%Y",
        "%d-%m-%Y",
        "%H:%M:%S",
        "%M:%S"
        ] 


for ft in formats:
    time = datetime.datetime.now()
    time = time.strftime(ft)
    print("Format",ft,": ", time)