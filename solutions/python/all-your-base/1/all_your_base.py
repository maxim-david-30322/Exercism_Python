def smaller_than_10(input_base, digits, output_base):
    power=len(digits)-1
    sum=0

    for d in digits:
        if d<0 or d>=input_base:
            raise ValueError("all digits must satisfy 0 <= d < input base")


        
        sum+=int(d)*int(input_base)**power
        power-=1
    
    return sum

def higher_than_10(input_base, digits, output_base):
    nr=[]
    rest=digits[0]%output_base
    cat=digits[0]//output_base
    nr.append(rest)
    while cat!=0:

        
        rest=cat%output_base
        cat=cat//output_base
        nr.append(rest)
    
    nr_baza=nr[::-1]

    return nr_baza




def rebase(input_base, digits, output_base):


    # for input.
    if input_base<2:
        raise ValueError("input base must be >= 2")


    # or, for output.
    if output_base<2:
        raise ValueError("output base must be >= 2")

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not digits or digits == [0]:
        return [0]

    # Step 1: convert from input base to decimal (an integer)
    decimal_value = smaller_than_10(input_base, digits, 10)

    # Step 2: convert from decimal to the target base digits
    # Even if output_base is 10, this will now return [4, 2] instead of [42]
    return higher_than_10(10, [decimal_value], output_base)

