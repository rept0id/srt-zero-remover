def main():
	filepath_output=''
	f= open(filepath_output,"w+")

	print("Enter/Paste your content. Ctrl-D or Ctrl-Z ( windows ) to save it.")
	contents = []
	while True:
		try:
			line = input()
		except EOFError:
			break
		contents.append(line)
	
	loop1_counter=0
	for i in contents:
		if (i.isdigit()) :
			contents[loop1_counter] = int(contents[loop1_counter]) + int(1)
		loop1_counter = loop1_counter + 1
		
	for i in contents:
		f.write(str(i) + '\n')
    
 main();
