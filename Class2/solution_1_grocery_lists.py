# Grocery lists items:

Pizza = 9.99
Pizza_qty = 2
Cola = .99
Cola_ltr = 4
Chicken_wings = .99
Chicken_wings_qty = 12
celery = .99
celery_qty = 2
breadsticks = 2.99
breadsticks_qty = 2

tax_rate = .077

# First purchase:

total = Pizza * Pizza_qty +  Cola * Cola_ltr
tax_total = total * tax_rate
grand_total = total + tax_total

print("Your purchase is:")
print("Pizza: %s" % Pizza_qty)
print("Cola: %s" % Cola_ltr)
print
print("Your subtotal is: %s" % total)
print("your tax is: %s" % tax_total)
print("Grand Total: %s" % grand_total)
print
print 

# second purchase

# decide to purchase an extra celery
celery_qty = celery_qty + 1
total = total + Chicken_wings * Chicken_wings_qty + celery * celery_qty
tax_total = total * tax_rate
grand_total = total + tax_total

print("Your purchase is:")
print("Pizza: %s" % Pizza_qty)
print("Cola: %s" % Cola_ltr)
print("Chicken_wings: %s" % Chicken_wings_qty)
print("celery: %s" % celery_qty)
print
print("Your subtotal is: %s" % total)
print("your tax is: %s" % tax_total)
print("Grand Total: %s" % grand_total)
print 
print

# third purchase
# actual I changed my mind, I just want breadsticks
celery_qty = celery_qty - 1
total = total + breadsticks * breadsticks_qty - celery 
tax_total = total * tax_rate
grand_total = total + tax_total

print("Your purchase is:")
print("Pizza: %s" % Pizza_qty)
print("Cola: %s" % Cola_ltr)
print("Chicken_wings: %s" % Chicken_wings_qty)
print("celery: %s" % celery_qty)
print("breadsticks: %s" % breadsticks_qty)
print
print("Your subtotal is: %s" % total)
print("your tax is: %s" % tax_total)
print("Grand Total: %s" % grand_total)
