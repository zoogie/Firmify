#!/usr/bin/env python
import hashlib
import glob

def int2string(n):
	str=bytearray(4)
	for i in range(4):
		str[i]=n & 0xFF
		n=n>>8
	return str
	
def zero(n):
	return (n*b"\x00")
	
def pad(n):
	return (n*b"\xFF")
	
def wait(s):
	try: 
		input(s)
	except:
		pass
	
def convert(path):
	a9entry=0x23F00000
	f1=open(path,"rb")
	file_buff=bytearray(f1.read())
	file_len=len(file_buff)
	pad_len=0x200-(file_len % 0x200)
	total_len=file_len+pad_len
	
	file_buff+=pad(pad_len)
	hash=hashlib.sha256(file_buff).digest()
	
	header=b"FIRM"+zero(8)+int2string(a9entry)
	header+=int2string(1) #arm11 suggest screeninit flag
	header+=zero(0x2C)
	header+=int2string(0x200)+int2string(a9entry)+int2string(total_len)+int2string(0)
	header+=hash
	header+=zero(0x190)
	
	path=path.replace(".bin",".firm")
	f2=open(path,"wb")
	f2.write(header+file_buff)
	f1.close()
	f2.close()
	print("created: "+path)

file_list=glob.glob("*.bin")

print("\nFIRMify - zoogie\nOnly intended for arm9 luma/payloads.\nNot for anything written to firm0/firm1 like boot9strap.\n")
wait("Press enter key to start FIRMification...")
for i in file_list:
	convert(i)
wait("done.")