"""Generate sales report showing total melons each salesperson sold."""

#create empty lists to store the data
# salespeople = []
# melons_sold = []

# #read in the file
f = open('sales-report.txt')

# #loop through the fils and split it at the vertical line
# for line in f:
#     line = line.rstrip()
#     entries = line.split('|')

#     #assisgn the sales person and melons to the indexes that they match
#     salesperson = entries[0]
#     melons = int(entries[2])

#     #check if salesperson is in the list and update their melons count,
#     #otherwise add them and their melon count to the list
#     if salesperson in salespeople:
#         position = salespeople.index(salesperson)

#         melons_sold[position] += melons
#     else:
#         salespeople.append(salesperson)
#         melons_sold.append(melons)

# #go through the lists and print off the information
# for i in range(len(salespeople)):
#     print(f'{salespeople[i]} sold {melons_sold[i]} melons')


#more efficient way to use the dictionary
melon_sales = {}
for line in f:
    line = line.rstrip()
    entries = line.split("|")

    salesperson = entries[0]
    melons = int(entries[2])

    melon_sales[salesperson] = melon_sales.get(salesperson, 0) + melons

for salesperson, melon_count in melon_sales.items():
    print(f"{salesperson} sold {melon_count} melons.")


