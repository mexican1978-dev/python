month = int(input("Enter number of month: "))
a = "winter"
b = "spring"
c = "summer"
d = "autumn"
four_seasons = [a, a, b, b, b, c, c, c, d, d, d, a]
print(four_seasons[month - 1])


four_seasons_2 = {1: a, 2: a, 3: b, 4: b, 5: b, 6: c, 7: c, 8: c, 9: d, 10: d, 11: d, 12: a}
print(four_seasons_2.get(month))

four_seasons_all = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
four_seasons_3 = {1: four_seasons_all[0],
                  2: four_seasons_all[1],
                  3: four_seasons_all[2],
                  4: four_seasons_all[3],
                  5: four_seasons_all[4],
                  6: four_seasons_all[5],
                  7: four_seasons_all[6],
                  8: four_seasons_all[7],
                  9: four_seasons_all[8],
                  10: four_seasons_all[9],
                  11: four_seasons_all[10],
                  12: four_seasons_all[11]
                  }
print(four_seasons_3.get(month))
