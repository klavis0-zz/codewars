#cc = input("Enter credit card number: ")  # cc for Credit Card


def maskify(cc):

    return "#"*(len(cc)-4) + cc[-4:]


#print(maskify(cc))

