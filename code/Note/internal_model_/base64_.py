import base64

print(base64.b64encode(b'aini,meishaonv'))
print(base64.b64decode(b'YWluaSxtZWlzaGFvbnY='))

print(base64.urlsafe_b64encode(b'aini/meishaonv'))
print(base64.urlsafe_b64decode(b'YWluaS9tZWlzaGFvbnY='))