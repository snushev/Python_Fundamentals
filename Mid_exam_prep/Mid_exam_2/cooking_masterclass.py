from math import ceil

budget = float(input())
students = int(input())
package_of_flour_price = float(input())
single_egg_price = float(input())
apron_price = float(input())

flour = (students - (students // 5)) * package_of_flour_price
eggs = 10 * students * single_egg_price
aprons = ceil(1.2 * students) * apron_price
total_cost = flour + aprons + eggs
if total_cost <= budget:
    print(f"Items purchased for {total_cost:.2f}$.")
else:
    print(f"{total_cost - budget:.2f}$ more needed.")



