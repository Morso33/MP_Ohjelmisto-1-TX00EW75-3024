seasons = ["kevät", "kesä", "syksy", "talvi"]
months = ["tammikuu", "helmikuu", "maaliskuu", "huhtikuu", "toukokuu", "kesäkuu", "heinäkuu", "elokuu", "syyskuu", "lokakuu", "marraskuu", "joulukuu"]

def get_season(month_name):
    month = months.index(month_name)
    if (month == 0 or month == 1 or month == 2):
        return seasons[0]
    elif (month == 3 or month == 4 or month == 5):
        return seasons[1]
    elif (month == 6 or month == 7 or month == 8):
        return seasons[2]
    else:
        return seasons[3]
    
print (get_season("joulukuu"))