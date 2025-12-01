salary = int(input('월급 입력 : '))
annual_salary = salary * 0 # 연봉

tax = 0.0 # 세금

if salary >= 500 :
    annual_salary = salary * 12
else:
    annual_salary = salary * 13

if 0<=annual_salary<=1000:
    tax = annual_salary * 1.0
elif 1000<=annual_salary<5000:
    tax = annual_salary * 0.1
elif 5000<=annual_salary<7000:
    tax = annual_salary * 0.12
elif 7000<=annual_salary<10000:
    tax = annual_salary * 0.15
else:
    tax = annual_salary * 0.20

print('급여 : %s ' % salary)
print('연봉 : %.2f ' % annual_salary)
print('세금 : %.2f ' % tax)
