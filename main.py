import sys
from time import*
Z,W=69000,51000
D={'P':(-10,-20,-11,-9),'N':(-19,-8,12,21,19,8,-12,-21),'B':(-9,11,9,-11),'R':(-10,1,10,-1)}
D['Q']=D['K']=D['B']+D['R']
Q=b'ddeginxdbdeg_bdfghfc^begbdefffedbdefddddeehfcdeebddeeeeebdeeld]XURPPedb`'
T={}
for k,p in enumerate('PNBRQK'):T[p]=[(100,300,320,500,930,60000)[k]+4*(Q[12*k+9-i//10]+Q[12*k+8+min(i%10-1,8-i%10)]-200)for i in range(120)]
def G(p):
 b,s,c,e,k=p
 for i,x in enumerate(b):
  for d in D.get(x,()):
   j=i
   while 1:
    j+=d;y=b[j]
    if y not in'.pnbrqk':break
    if x=='P':
     if d in(-10,-20)and y!='.'or d==-20 and(i<81 or b[i-10]!='.')or d in(-11,-9)and y=='.'and j not in(e,k-1,k,k+1):break
     if j<29:
      for r in'NBRQ':yield i,j,r
      break
    yield i,j,''
    if x in'PNK'or y!='.':break
    if i==91 and b[j+1]=='K'and c&1:yield j+1,j-1,''
    if i==98 and b[j-1]=='K'and c&2:yield j-1,j+1,''
def V(p,m):
 b,s,c,e,k=p;i,j,r=m;x=b[i];y=b[j];v=T[x][j]-T[x][i]
 if y.islower():v+=T[y.upper()][119-j]
 if abs(j-k)<2:v+=T['K'][119-j]
 if x=='K'and abs(i-j)==2:v+=T['R'][(i+j)//2]-T['R'][91 if j<i else 98]
 if x=='P':
  if j<29:v+=T[r][j]-T['P'][j]
  if j==e:v+=T['P'][109-j]
 return v
def R(p):
 b,s,c,e,k=p
 return b[::-1].swapcase(),-s,c>>2|(c&3)<<2,119-e if e else 0,119-k if k else 0
def mv(p,m):
 b,s,c,e,k=p;i,j,r=m;x=b[i];s+=V(p,m);a=list(b);a[j]=x;a[i]='.';E=K=0
 c&={91:14,98:13}.get(i,15)&{21:7,28:11}.get(j,15)
 if x=='K':
  c&=12
  if abs(i-j)==2:K=(i+j)//2;a[91 if j<i else 98]='.';a[K]='R'
 if x=='P':
  if j<29:a[j]=r
  if j-i==-20:E=i-10
  if j==e:a[j+10]='.'
 return R((''.join(a),s,c,E,K))
A=lambda q:any(q[0][j]=='k'or abs(j-q[4])<2 for _,j,_ in G(q))
def B(p,g,d,r=0):
 global n
 n+=1
 if n%512<1 and(n>L or time()>X):1/0
 d=max(d,0)
 if p[1]<=-W:return-Z
 if d and not r and p in H:return 0
 e=S.get((p,d,r),(-Z,Z))
 if e[0]>=g and(not r or p in M):return e[0]
 if e[1]<g:return e[1]
 def f():
  if d>2 and not r and any(c in p[0]for c in'RBNQ'):yield 0,-B(R(p[:3]+(0,0)),1-g,d-3)
  if d<1:yield 0,p[1]
  k=M.get(p)
  if k and(d or V(p,k)>=60):yield k,-B(mv(p,k),1-g,d-1)
  for v,m in sorted(((V(p,m),m)for m in G(p)),reverse=True):
   if d or v>=60:yield m,-B(mv(p,m),1-g,d-1)
 b=-Z
 for m,s in f():
  b=max(b,s)
  if b>=g:
   if m:M[p]=m
   break
 if d>2 and b==-Z:b=-W if A(R(p[:3]+(0,0)))else 0
 S[p,d,r]=(b,e[1])if b>=g else(e[0],b)
 return b
q=lambda m:ord(m[0])+4-10*int(m[1])
u=lambda i:chr(96+i%10)+str(10-i//10)
H=set();S={};M={};n=L=X=Y=0
l='position startpos'
while l:
 t=l.split()+['']
 c=t[0]
 if c=='uci':print('id name t\nuciok')
 if c=='isready':print('readyok')
 if c=='position':
  z=t.index('moves')if'moves'in t else len(t)-1
  f=t[2:z]if t[1]=='fen'else'rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq -'.split()
  r=f[0]
  for k in'12345678':r=r.replace(k,'.'*int(k))
  b=' '*20+''.join(' '+x+' 'for x in r.split('/'))+' '*20
  P=b,sum(T[x][i]for i,x in enumerate(b)if x.isupper())-sum(T[x.upper()][119-i]for i,x in enumerate(b)if x.islower()),sum(2**'QKkq'.index(x)for x in f[2]if x>'-'),0 if f[3]=='-'else q(f[3]),0
  o=f[1]=='b'
  if o:P=R(P)
  H={P}
  for m in t[z+1:-1]:
   i,j=q(m[:2]),q(m[2:4])
   if o:i,j=119-i,119-j
   P=mv(P,(i,j,m[4:].upper()));o=not o;H.add(P)
 if c=='go':
  g=dict(zip(t[1::2],t[2::2]))
  x=float(g.get('movetime',0))/1e3 or float(g.get('btime'if o else'wtime',15e4))/3e4
  x=min(x,8,(1700-Y)/30);t0=time();X=t0+min(x*1.5,8.5);L=x*7e4;n=0;S={};M={}
  LM=[m for m in G(P)if not A(mv(P,m))]
  try:
   a=0
   for d in range(1,int(g.get('depth',99))+1):
    lo,hi=-W,W
    while lo<hi-15:
     s=B(P,a,d,1)
     if s>=a:lo=s
     else:hi=s
     a=(lo+hi+1)//2
  except:0
  m=M.get(P)
  if m not in LM:m=LM[0]if LM else 0
  Y+=time()-t0
  if m:i,j,r=m;print('bestmove',u(119-i if o else i)+u(119-j if o else j)+r.lower())
  else:print('bestmove 0000')
 if c=='quit':break
 sys.stdout.flush();l=sys.stdin.readline()
 