#If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
#how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) 
#contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
#The use of "and" when writing out numbers is in compliance with British usage.

def numLetterCount():
    ones_letter_count = [0,3,3,5,4,4,3,5,5,4,3,6,6,8,8,7,7,9,8,8] # [ -, "one" = 3, "two" = 3, "three" = 5, etc...]
    tens_letter_count = [0,3,6,6,5,5,5,7,6,6]
    hundred = 7
    thousand = 8
    answer = 0
    for i in range(1,1000):
        ones_place = i % 10
        tens_place = ((i % 100) - ones_place) / 10
        hundreds_place = ((i % 1000) - (tens_place * 10) - ones_place) / 100
        if hundreds_place != 0:
            answer += ones_letter_count[hundreds_place] + hundred
            if tens_place != 0 or ones_place != 0: answer += 3 #"and"
        if tens_place == 0 or tens_place == 1: 
            answer += ones_letter_count[tens_place * 10 + ones_place]
        else: 
            answer += tens_letter_count[tens_place] + ones_letter_count[ones_place]
    
    answer += ones_letter_count[1] + thousand #adds 1000
    
    return answer
    
if __name__ == '__main__':
    print(numLetterCount())
