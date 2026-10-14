def calculateElectronicsGST(a , b):
    total =a + b 
    gst =total * 0.18
    return total + gst

def calculateFashionGST(c , d):
    total = c + d
    gst = total * 0.13
    return total + gst

def calculateFoodGST(e):
    gst = e * 0.07
    return e + gst

def totalBill(a , b , c , d , e):
    electronics = calculateElectronicsGST(a , b)
    fashion = calculateFashionGST(c , d)
    food = calculateFoodGST(e)

    return electronics + fashion + food

def calculateDiscountedBill(a , b , c , d , e):
    total = totalBill(a , b , c , d , e)
    discount = total * 0.20 
    final_amount = total - discount

    return final_amount

a = 100
b = 100
c = 100
d = 100
e = 100

electronics = calculateElectronicsGST(a , b)
fashion = calculateFashionGST(c , d)
food = calculateFoodGST(e)

total = totalBill(a , b , c , d , e)
discount = total * 0.20 
final_amount = calculateDiscountedBill(a , b, c , d , e)

print("Electronics Bill with GST: Rs", format(electronics, ".2f"))
print("Fashion Bill with GST: Rs", format(fashion, ".2f"))
print("Food Bill with GST: Rs,", format(food,".2f"))
print("Total Bill after GST: Rs.", format(total, ".2f"))
print("Discount on Total Bill: Rs.", format(discount, ".2f"))
print("Final Payable Amount; Rs.", format(final_amount, ".2f"))