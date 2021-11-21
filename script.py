import csv

with open("flags.tsv") as tsv_file:
    read_tsv = csv.reader(tsv_file, delimiter="\t")
    next(read_tsv, None) # skip the headers
    for row in read_tsv:
        num = row[0]
        question = row[1]
        typ = row[2]
        points = row[3]
        flag = row[4]
        chall = row[5]
        solution = row[6]
        outFile = num.zfill(2) + '. ' + question + '.md'
        with open(outFile,'w') as out:  
            out.write('## %s (%s %s pts)  \n' % (question, typ, points))
            out.write('### Challenge:  \n')
            out.write('```\n')
            for line in chall.split('\\n'):
                out.write('%s  \n' % line)
            out.write('```\n')
            out.write('  \n')
            out.write('### Solution:  \n')
            for line in solution.split('\\n'):
                out.write('%s  \n' % line)                      
            out.write('  \n')
            out.write('Flag: `%s`  \n' % flag)
            out.write('  \n')
            out.close()

tsv_file.close()

'''
sh > cat "01 The Wave of Us.md"
## The Wave of Us (forensics 50 pts)
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


Flag: `flag{this_is_a_fake_flag}`

'''
