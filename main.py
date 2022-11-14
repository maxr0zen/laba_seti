def output_convertor(inputer, outputer):
    for item in inputer:
        outputer += str(item) + '.'
    outputer = outputer[0:-1]
    return outputer


                #Cчитывание IP
ip_address = []
a, b, c, d = map(int, input('Введите ip: ').split('.'))
ip_address.append(a); ip_address.append(b); ip_address.append(c); ip_address.append(d)
for i in ip_address:
    if i > 255: print("Вы неправильно ввели IP"), exit()


                                                                                                #Считывание Маски
a = int(input('Введите маску: '))
if a > 32: print("Вы неправильно ввели маску"), exit()
bin_mask_str = a*'1' + ((32-a)*'0')
bin_mask = []
bin_mask.append(bin_mask_str[0:8]), bin_mask.append(bin_mask_str[8:16]), bin_mask.append(bin_mask_str[16:24])\
    , bin_mask.append(bin_mask_str[24:32])


                                                                                                #Нормальный вид Маски
mask = []
mask_output = ''
mask += [int(item, base=2) for item in bin_mask]
reversed_mask = []
reversed_mask += [255-item for item in mask]

print('Маска в нормальном виде: ', output_convertor(inputer=mask,outputer=mask_output))




                                                                                                #Адресс сети
set_adress = []
output_adress = ''
set_adress += [ip_address[item] & mask[item] for item in range(4)]
print('Адрес сети: ',output_convertor(inputer=set_adress, outputer=output_adress))


                                                                                                #Широковещательный адресс
shir_adress = []
output_shir = ''
shir_adress += [set_adress[item] + reversed_mask[item] for item in range(4)]
print('Широковещательный адресс: ', output_convertor(inputer=shir_adress, outputer=output_shir))


                #Количество хостов
print('Количество хостов: ', (2**(32 - a)))


