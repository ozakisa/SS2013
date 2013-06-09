import sys,os

argvs = sys.argv     #コマンドライン引数の取得
argc = len(argvs) 	#コマンドライン引数の個数の取得

#もし argcが適正でないときには
if (argc != 3): 
    print 'Usage: $ python %s target_file making_file' % argvs[0]
    quit()
#コメント表示して終了

#適正なときは
f = open(argvs[1]) 	#対象ファイルから
s = f.read() 	#全てリストに読み込んで一行ごとに処理
f.close() 		#ファイル閉じる

words = s.split()

d = {}

for w in words: 
    if d.has_key(w):
        d[w] += 1
    else: 
        d[w] = 1


sored_keys = sorted(d.keys(), key = lambda x: d[x], reverse = True)
print "all: %d" % len(d)

i = 0
for k in sored_keys:
    if i == 20:
        break
    print k, ": ", d[k]
    i += 1



