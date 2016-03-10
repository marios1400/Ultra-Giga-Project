k=True
while k==True:
    points1=0
    points2=0
    a=raw_input("Give the first profile")
    b=raw_input("Give the second profile")
    c=a.find("TWEETS")
    d=a.find("FOLLOWING")
    e=a.find("FOLLOWERS")
    f=a.find("LIKES")
    c1=c+6
    c2=d-2
    d1=d+9
    d2=e-2
    e1=e+9
    e2=f-2
    f1=f+5
    tweets1=a[c1:c2]
    following1=a[d1:d2]
    followers1=a[e1:e2]
    likes1=a[f1: ]
    g=b.find("TWEETS")
    h=b.find("FOLLOWING")
    i=b.find("FOLLOWERS")
    j=b.find("LIKES")
    g1=g+6
    g2=h-2
    h1=h+9
    h2=i-2
    i1=i+9
    i2=j-2
    j1=j+5
    tweets2=b[g1:g2]
    following2=b[h1:h2]
    followers2=b[i1:i2]
    likes2=b[j1: ]
    if tweets1[-1]=="K":
        tweets1=float(tweets1[:-1])
        tweets1=tweets1*1000
    elif tweets1[-1]=="M":
        tweets1=float(tweets1[:-1])
        tweets1=tweets1*1000000
    if tweets2[-1]=="K":
        tweets2=float(tweets2[:-1])
        tweets2=tweets2*1000
    elif tweets2[-1]=="M":
        tweets2=float(tweets2[:-1])
        tweets2=tweets2*1000000
    if float(tweets1)>float(tweets2):
        points1=points1+1
    elif float(tweets1)<float(tweets2):
        points2=points2+1
    if following1[-1]=="K":
        following1=float(following1[:-1])
        following1=following1*1000
    elif following1[-1]=="M":
        following1=float(following1[:-1])
        following1=following1*1000000
    if following2[-1]=="K":
        following2=float(following2[:-1])
        following2=following2*1000
    elif following2[-1]=="M":
       following2=float(following2[:-1])
       following2=following2*1000000
    if float(following1)>float(following2):
        points1=points1+1
    elif float(following1)<float(following2):
        points2=points2+1
    if followers1[-1]=="K":
        followers1=float(followers1[:-1])
        followers1=followers1*1000
    elif followers1[-1]=="M":
        followers1=float(followers1[:-1])
        followers1=followers1*1000000
    if followers2[-1]=="K":
        followers2=float(followers2[:-1])
        followers2=followers2*1000
    elif followers2[-1]=="M":
        followers2=float(followers2[:-1])
        followers2=followers2*1000000
    if float(followers1)>float(followers2):
        points1=points1+1
    elif float(followers1)<float(followers2):
        points2=points2+1
    if likes1[-1]=="K":
        likes1=float(likes1[:-1])
        likes1=likes1*1000
    elif likes1[-1]=="M":
        likes1=float(likes1[:-1])
        likes1=likes1*1000000
    if likes2[-1]=="K":
        likes2=float(likes2[:-1])
        likes2=likes2*1000
    elif likes2[-1]=="M":
        likes2=float(likes2[:-1])
        likes2=likes2*1000000
    if float(likes1)>float(likes2):
        points1=points1+1
    elif float(likes1)<float(likes2):
        points2=points2+1
    print "The score is:",points1,"-",points2
    k=raw_input("Do you want to continue? YES or NO")
    if k=="YES":
        k=True
    else:
        k=False
    
