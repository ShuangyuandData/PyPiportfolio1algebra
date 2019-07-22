from matrixalgebrasge import MatrixA

Ma1=MatrixA()
Ma1.read_data_file('M1.txt')
print(Ma1.nrow)
print(Ma1.ncol)
Ma1.print_matrix()
print(Ma1.data_matrix[0][0])

print('--------------')
print('--------------')
print('--------------')
Ma2=MatrixA()
Ma2.read_data_file('M2.txt')
Ma2.print_matrix()

Ma3=MatrixA()
Ma3.read_data_file('M3.txt')

Ma4=MatrixA()
Ma4.read_data_file('M4.txt')


print('--------------')
Ma5=Ma1 + Ma2
Ma5.print_matrix()

print('--------------test1')
Ma6=Ma1 + Ma3

print('--------------test2')
Ma7=Ma1 - Ma2
Ma7.print_matrix()

print('--------------test3')
Ma8=Ma1 - Ma4


print('--------------test4')
Ma9=Ma1 * Ma2
Ma9.print_matrix()

print('--------------test5')
Ma10=Ma1 * Ma3


print('--------------test6')
Ma11=Ma1 * Ma4
Ma11.print_matrix()

print('--------------test7')

print(Ma3.det())
Ma12=Ma3.inv()
Ma12.print_matrix()


