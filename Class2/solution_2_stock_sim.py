stock_price = 100
month1 = .01
month2 = .02
month3 = .03
month4 = -.01
month5 = -.02
month6 = -.03
month7 = .5
month8 = .25
month9 = -.5
month10 = .02
month11 = .03
month12 = .05


q1 = stock_price * (1 + month1) * (1 + month2) * (1 + month3)
q2 = q1 * (1 + month4) * (1 + month5) * (1 + month6)
q3 = q2 * (1 + month7) * (1 + month8) * (1 + month9)
q4 = q3 * (1 + month10) * (1 + month11) * (1 + month12)

print("q1:" + str(q1))
print("q2:" + str(q2))
print("q3:" + str(q3))
print("q4:" + str(q4))