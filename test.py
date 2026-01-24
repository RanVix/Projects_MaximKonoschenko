string = 'апельсины 45 991 63 100 12 яблоки 13 47 26 0 161'
new_string = string.split()
result = {}
word = ''

for item in new_string:
    if item.isalpha():
        word = item
        result[word] = []
    else:
        result[word].append(int(item))

def find_max_sales(sales_dict):
    max_sales = {}

    for product in sales_dict:
        max_sales[product] = max(sales_dict[product])
    return max_sales

print(result)
print(find_max_sales(result))