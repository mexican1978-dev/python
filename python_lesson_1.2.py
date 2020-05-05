time = int(input("Enter your seconds: "))
seconds = time % 60
if seconds < 10:
    seconds = '0' + str(seconds)
minutes = time // 60 % 60
if minutes < 10:
    minutes = '0' + str(minutes)
hours = time // 3600 % 24
if hours < 10:
    hours = '0' + str(hours)
print(f"{hours}:{minutes}:{seconds}")









