with open('topics.txt', 'w') as output_file:
    output_file.write('Computer Science')

# we can append without overweite the existing content by using 'a'
with open('topics.txt', 'a') as output_file:
    output_file.write(' & Software Engineerng')

with open('topics.txt', 'r') as read_topics:
    contents = read_topics.read()

print(contents)