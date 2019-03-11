cc = input("Enter credit card number: ")  # cc for Credit Card


def maskify(cc):

    return cc.replace(cc[0:-4], "#")


print(maskify(cc))
