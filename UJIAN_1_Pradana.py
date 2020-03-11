########## PRADANA INDRA ##########

### NUMBER 1 ###

# inputan = input('Masukan Kata/Kalimat: ')

# def hashtag(string):
#     hasil = '#'
#     for kata in string.split():
#         hasil += kata.capitalize()
#     if len(hasil) > 140:
#         print('False')
#     elif hasil == '#':
#         print('False')
#     else:
#         print(hasil)

# hashtag(inputan)
# hashtag('hello there how are you doing')
# hashtag('')
# hashtag('prajobnoejbjbejbakjbbfjebkakbekfbekjkajbakbkwebdfajnwfkjbnakewfbkjbefbkjebfjbewflkbjbnejbfkjbqkjnbsjkbdkbkebfkdjabkjbfkqebjbkjdblnaljnsjbfebbejbkfjanldnlenwlfljslanonlencjbakdbkbwkdbljnljaskfbjbekbkjebfwbkjbdkbjwbFBKWEBFKBKBDKQBEKFBKQSBKDBEKBFKJWBEFKBWKBEFKBKDBKBKbkbekwfbkwbfkbwrbfkbwbfkwrbfkbwkebfkbrwkfksbjhvkwbkhgvkhbsjbckhgeibfkwbbvkwebfkbwkjkckvjkbwkkwjbekebckbwkejbkfbkjsbdkbckwbckbdskbfkwbkcwkjrkwnfwejcbkfbwejkbfkewvbfkjwbekcwk')



### NUMBER 2 ###

# def phone_num(number):
#     if len(number) == 10:
#         print('({}{}{}) {}{}{}-{}{}{}{}'.format(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]))
#     else:
#         print('Error')


# phone_num([1,2,3,4,5,6,7,8,9,0])


### NUMBER 3 ###
# ODD NUMBER ASCENDING SAME INDEX
# EVEN NUMBER DESCENDING SAME INDEX

# def sort_odd_even(n):
#     n_odd = []
#     n_even = []

#     for idx,val in enumerate(n):
#         if val % 2 > 0:
#             n_odd.append(val)
#         else:
#             n_even.append(val)

#     for i in range(len(n_odd)):
#         for j in range(i+1, len(n_odd)):
#             if n_odd[i] > n_odd[j]:
#                 n_odd[i], n_odd[j] = n_odd[j], n_odd[i]
#             else:
#                 pass

#     for k in range(len(n_even)):
#         for l in range(k+1, len(n_even)):
#             if n_even[k] < n_even[l]:
#                 n_even[k], n_even[l] = n_even[l], n_even[k]
#             else:
#                 pass
    

#     idx_odd = []
#     idx_even = []

#     for idx,val in enumerate(n):
#         if val % 2 > 0:
#             idx_odd.append(idx)
#         else:
#             idx_even.append(idx)

#     z = zip(idx_odd,n_odd)
#     x = zip(idx_even,n_even)

#     hasil = [0 for banyaknya in range(len(n))]

#     for posisi, angka in z:
#         hasil[posisi] = angka
#     for pos, ang in x:
#         hasil[pos] = ang




#     print(hasil)
#     # print(z)
#     # print(idx_odd)
#     # print(idx_even)
#     # print(n_odd)
#     # print(n_even)

# sort_odd_even([5,3,2,8,1,4])
        
        

### NUMBER 4 ###

# def hollowTriangle(n):
#     if n == 1:
#         print("#")
#         return False

#     top = ["_" * (n - 1) + "#" + "_" * (n - 1)]  
#     print(top[0])


#     mid =[]
#     for i in range(n - 2, 0, -1):
#         mid.append(("_" * i) + "#" + ("_" * ((2 * n) - (2 * i) - 3)) + "#" + ("_" * i))
#     for i in mid:
#         print(i)

#     bot = ["#" * ((2 * n) - 1)]
#     print(bot[0])  

# hollowTriangle(7) 
# hollowTriangle(1)
# hollowTriangle(2) 
# hollowTriangle(3)
# hollowTriangle(4) 
# hollowTriangle(5)
# hollowTriangle(6)








    



