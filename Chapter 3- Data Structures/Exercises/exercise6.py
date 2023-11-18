guest_list= ['khatira' , 'Maha' , 'Noor']
print('sorry guys i can only invite two people to the dinner.')
print('sorry sister ' + guest_list[1]+ ' you are not ivited for dinner.')
guest_list.pop(1)
print(guest_list)

print('dear '+ guest_list[0] + ' you are still ivited to the dinner')
print('dear '+ guest_list[1] + ' you are still ivited to the dinner')

del guest_list[:]
print('guest_list:' , guest_list)