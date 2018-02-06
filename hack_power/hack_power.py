#!/usr/bin/env python

#### function "count_letter" count power of singular letter in hack
def count_letter(hack=str, letter=vars, power=int):
    count_letter = hack.count(letter)
    i=0
    sum=0
    while i < (count_letter)*power:
        i=i+power
        sum+=i
    return sum

#### function "count_phrase" count power of singular phrase in hack
def count_phrase(hack=str, phrase=str, power=int):
    sum=hack.count(phrase)*power
    return sum

#### function "sum_letters" sum power of all letters in hack
def sum_letters(hack, letters=dict()):
    sum = 0
    for i in letters:
        sum += count_letter(hack, i, letters[i])
    return sum

#### function "sum_phrases" sum power of all phrases in hack
def sum_phrases(hack, phrases=dict()):
    phrases_copy = phrases.copy()
    for i in phrases:               #### this loop is us in sytuation when short phrase is in deferent longer phrase to not count short phrases
        for j in phrases:
            if j!=i and j in i and i in hack:
                    phrases_copy[j]=0
    sum=0
    for i in phrases_copy:
        sum+=count_phrase(hack, i, phrases_copy[i])
    for i in phrases:               #### this loop is us in sytuation when short phrase is in deferent longer but short phrase is exist in hack in deferent part of hack
        for j in phrases:
            if j!=i and j in i and i in hack:
                if hack.count(j)>hack.count(i):
                    sum+=phrases[j]
    return sum


#### function "full_power" is sum power of all letters and phrases in hack
def full_power(hack=str, letters=dict(), phrases=dict()):
    count_letters_form_dict=0
    for i in letters:                           #### this loop is count how meny letters form dictionary is in hack
        count_letters_form_dict+=hack.count(i)
    if count_letters_form_dict == len(hack):    #### this condition is chacking that are diffrent letters in hack that in letters dictionary
        return sum_letters(hack, letters) + sum_phrases(hack, phrases)
    else:
        return 0
#### function "hack_calculator" is print resalt
def hack_calculator(hack=str, letters=dict(), phrases=dict()):
    print('​  Hack %s is worth %s power.' %(hack, full_power(hack, letters, phrases)))


if __name__ == "__main__":  

    hack_calculator(hack='baacacccbaaaccccbababa', letters={"a":1, "b":2, "c":3}, phrases={"baa":20, "ba":10})
