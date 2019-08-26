import requests
req = requests.get('https://www.google.com/url?sa=i&rct=j&q=&esrc=s&source=images&cd=&ved=2ahUKEwiwzI2a3Z_kAhUGv48KHfYZC1sQjRx6BAgBEAQ&url=https%3A%2F%2Funsplash.com%2Fsearch%2Fphotos%2Fbridge&psig=AOvVaw0shTpWzaEHBVyJ7SOysfs4&ust=1566881121247517',stream=True)
req.raise_for_status()
with open('image.jpg', 'wb') as fd:
    for chunk in req.iter_content(chunk_size=50000):
	print('Received a Chunk')
        fd.write(chunk)
