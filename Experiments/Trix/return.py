inntekt = float(input("Penger?"))
def foo(inntekt):
    if inntekt < 10000:
        skatt = inntekt * 0.1
        return skatt
    elif inntekt >= 10000:
        skatt = 0.3*(inntekt-10000)+100
        return skatt
    else:
         print(inntekt + "er en ugyldig besvarelse")
         return False

print("Netto" + str(inntekt - foo(inntekt)))
input()
