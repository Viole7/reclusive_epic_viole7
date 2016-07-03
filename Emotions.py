# This is my shitty attempt at coding.

feeling = input('How are you feeling?:  ')

bad_response = 'I\'m sorry to hear you\'re feeling {}!'.format(feeling)
good_response = 'I\'m glad to hear you\'re feeling {}!'.format(feeling)
g_emotions = ["good", "great"]
b_emotions = ["bad", "terrible"]


if (feeling in g_emotions):
    print(good_response)

elif (feeling in b_emotions):
    print(bad_response)

else:
    new_feeling = input('I\'ve never felt like that before, is {} good or bad?'.format(feeling))
    if new_feeling == min(g_emotions) and feeling != min(b_emotions) : g_emotions.append(feeling) , print(good_response)
    if new_feeling == min(b_emotions) and feeling != min(b_emotions) : b_emotions.append(feeling) , print(bad_response)

print(g_emotions)
print(b_emotions)
