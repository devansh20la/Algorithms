def sum(inputs, target ):
    
    def check(comb, idx):
        if idx + 1 > len(inputs):
            return
        choice1 = inputs[idx] + inputs[idx+1]
        choice2 = inputs[idx] - inputs[idx+1]
        choice3 = inputs[idx]*10 + inputs[idx+1]
        
        for c in [choice1, choice2, choice3]:
            if comb + c == target:
                print(f"{comb}+{c}")
            else:
                check(comb + c, idx+1)

            if comb - c == target:
                print(f"{comb}-{c}")
            else:
                check(comb + c, idx+1)
    
    for comb in [f"-{inputs[0]}", f"{inputs[0]}"]: 
        check(comb, 1)

sum([1,2,3], 6)
