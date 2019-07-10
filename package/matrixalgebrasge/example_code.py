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
print('--------------')
Ma3=Ma1 + Ma2
Ma3.print_matrix()

print('--------------')
Ma4=Ma1 - Ma2
Ma4.print_matrix()

print('--------------')
Ma5=Ma1 * Ma2
Ma5.print_matrix()
