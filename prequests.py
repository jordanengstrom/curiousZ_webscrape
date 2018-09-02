import requests

res = requests.get('http://automatetheboringstuff.com/files/rj.txt')

# Error handling
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))

# Open file in 'write binary' mode
playFile = open('RomeoAndJuliet.txt', 'wb')

# iter_content returns "chunks" of the content on each iteration through the loop.
# Each chunk is of bytes data type. 100000 bytes/chunk
for chunk in res.iter_content(100000):
    playFile.write(chunk)

# Closes the file
playFile.close()