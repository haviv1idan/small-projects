import webbrowser
try:
	from googlesearch import search
except ImportError:
	print("No module named 'google' found")

# to search
query = input('Enter dictionary entry to search: ')

flag = False
for j in search(query, tld="co.in", num=10, stop=10, pause=2):
	if "wikipedia" in str(j):
		webbrowser.open_new(j)
		flag = True
		break
	print(j)

if not flag:
	print("There is not an result to this search")
