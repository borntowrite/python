def strstr(string, sub):
    for i in range(len(string)-len(sub)+1):
        if string[i:i+len(sub)] == sub:
            return i

print(strstr("melongkakao", "kaka"))