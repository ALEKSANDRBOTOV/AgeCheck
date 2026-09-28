print("Укажи год и месяц, каждое в новой строке")
year=int(input())
month=int(input())
def days_in_month(year, month):
    if(month==4 or month==6 or month==9 or month==11):
        return (30)
    elif(month==2 and ((year%400)==0 or (year%4)==0 and (year%100)!=0)):
        return (29)
    elif(month==2):
        return(28)
    else:
        return(31)
print (days_in_month(year, month))