string = input("Введите строку для изменений 1-ого и последнего символа: ")

lines = string.split(' ')
modified_lines = []

for line in lines:
    
    if len(line) > 1:
        
        modified_line = line[-1] + line[1:-1] + line[0]
        
    else:
        
        modified_line = line
        
    modified_lines.append(modified_line)
    
modified_text = ' '.join(modified_lines)

print(f"Измененный текст: {modified_text}")