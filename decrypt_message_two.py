encrypted_file = open("encrypted_message_two.txt", 'r')

encrypted_message = encrypted_file.readline()

encrypted_file.close()

# Write Code Here
split_message = [encrypted_message[i] for i in range(len(encrypted_message))]
split_message_action = [encrypted_message[i] for i in range(len(encrypted_message))]
split_message_action.reverse()

for i in range(len(split_message)):
    if i%2 != 0:
        split_message[i] = split_message_action[i]
decrpted_message = ''.join(split_message)
print(decrpted_message)