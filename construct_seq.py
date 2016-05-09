import ocsv
import sys

# argv[1] - input file
# argv[2] - name of the column to be flipped
# argv[3] - output file

fin = open("C:\\Users\\AadarshSam\\Desktop\\CAPSTONE PROJECT_SCRIPTS\\PID.csv", 'r')


col = ocsv.getColumns(fin.readline())
flipCol = col['daystonext']
flipCol2=col['agyradm']
flipcol3=col['Gender']
currentpid = ''
# list of list of list
seqs = []
def func(line):
  global currentpid, seqs
  row = line.strip().split(',')
  #print row[flipCol2]
  pid = row[col['PID']]
  if pid == currentpid:
    seqs[-1][0].append(row[flipCol])

    seqs[-1][1].append(row[col['cost\n']])
  else:
    seqs.append([[row[flipCol]], [row[col['cost\n']]]])

  currentpid = pid
ocsv.runFunc(fin, func)
fin.close()
#print seqs

#print seqs



freq = dict()
fout = open("C:\\Users\\AadarshSam\\Desktop\\CAPSTONE PROJECT_SCRIPTS\\my_output.csv", 'w')

final_list=[]
trial_list=[]
for seq in seqs:
  #print seq[1]
  # skip sequence longer than 100
  if len(seq[0]) >= 50: continue
  # take the last 7 items only
  #if len(seq[0]) > 7: seq[0] = seq[0][-7:]
  for i in range(len(seq[0])):
    for j in range(len(seq[0]) - i):
      #print len(seq[0])
      key = ','.join(seq[0][j:j + i + 1]) + ',' + seq[1][j + i]
      #print len(key)
      print key


      dum = fout.write(key + '\n')
      if key in freq:
        freq[key] = freq[key] + 1
      else:
        freq[key] = 1

fout.close()

posseqs = []
for item in freq.items():
  if item[0][-1] == '1':
    key = item[0][0:-1] + '0'
    if key not in freq: continue
    count0 = freq[key]
    prob = item[1] / (item[1] + count0)
    if prob > 0.5: posseqs.append(item[0])
