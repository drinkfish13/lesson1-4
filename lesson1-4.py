salary = int(input())
ipoteka = int(input())
life = int(input())
bonus = int(input())
salary_year = salary*12
bonus_year = salary*bonus
nakoplenia_bonus = bonus_year/2

life_year = salary_year*life/100
ipoteka_year = salary_year*ipoteka/100

rashody_year = life_year + ipoteka_year
print(ipoteka_year)
print(salary_year - rashody_year + nakoplenia_bonus)