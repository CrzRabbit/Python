import re

# pattern = "^M{0:3}?(CM|CD|D?C{0:3})(XC|XL|L?X{0:3})(IX|IV|V?I{0:3})$"
# re.search(pattern, "")
# re.search(pattern, "M")
# re.search(pattern, "MM")
# re.search(pattern, "MMM")
# re.search(pattern, "MMMM")

phonePattern = re.compile(r"^\D*(\d{3})\D*(\d{3})\D*{\d{4}}\D*{\d*}$")
re.search(phonePattern, "800-400-1212")