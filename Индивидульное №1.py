
if __name__ == '__main__':
     n =int(input("Кол-во израсходованной электроэнергии=" )  
     if n <= 200:
        coast = 7 * n     
     elif n > 250 and n <= 300:
        coast = 7 * 250 + 17 * (n - 250)   
     else:
        coast = 7 * 250 + 20 * (n - 250)
print("Подсчитанная плата по тарифу = ", coast)
