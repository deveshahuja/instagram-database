# -*- coding: utf-8 -*-


import psycopg2


def q1():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with likedlist as ( select tagname,count(username)*0.3 as liked from (postlike natural join posttaged) where username='deveshahuja9' group by tagname order by count(username) desc ) select tagname,count(username)*0.6+liked as suggestdedindex from (saved natural join posttaged natural join likedlist) where username='deveshahuja9' group by tagname,liked order by (count(username)*0.3+liked*0.6) desc;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q2():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with plist as (	select postid,username	from post natural join users where not privacystatus	union	select postid,followsusername	from ((users natural join follows) as u join post as z on u.followsusername=z.username)	where u.username='deveshahuja9') select y.postid,location from (plist as x join post as y on x.postid=y.postid) group by location,y.postid order by location asc;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q3():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with list as ( Select  username,followsusername  from Follows  where Username='deveshahuja9') select distinct l.followsusername from (Follows as f join list as l on f.username=l.followsusername ) where f.followsusername='ankit_aahil' ;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q4():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; select tagname,count(username) from tagfollow group by tagname order by count(username) desc limit 5;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q5():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; select s.storyid from ((users natural join follows) as f join story as s on f.followsusername=s.username) where f.username='deveshahuja9' and extract(hour from s.timestamp)<24;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q6():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; Select Tagname,count(*) from Story natural join Storyreply natural join StoryTaged where Username ='rastogijii' group by Tagname;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def q7():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; select distinct tagname,count(tagname) from post natural join posttaged natural join comment group by tagname,commentusername,commenttimestamp order by count(tagname) desc;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def q8():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with followinglist as (select username,followsusername from follows where username='ankit_aahil') Select senderUsername, receiverUsername,count(*) as co from (Messages as x join followinglist as y on x.receiverUsername=y.followsusername) where senderUsername = 'ankit_aahil' or receiverUsername='ankit_aahil' group by senderUsername, receiverUsername order by co desc;")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def q9():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with followinglist as (select followsusername from follows where username='deveshahuja9') select distinct y.followsusername from (followinglist as x join follows as y on x.followsusername=y.username) except (select followsusername from followinglist  union  select username from users where username='deveshahuja9');")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def q10():
    
    conn = None
    try:
        """params = config()
        conn = psycopg2.connect(**params)"""
        
        
        conn = psycopg2.connect(host="10.100.71.21",database="201701018", user="201701018", password="201701018")

        
        cur = conn.cursor()
        cur.execute("set search_path to instagram ; with countlist as (select x.postid,count(x.postid) no_of_likes from (post as x join postlike as y on x.postid=y.postid) group by x.postid order by count(x.postid) desc) select postid,no_of_likes,username from (postlike natural join countlist);")
        row = cur.fetchone()
 
        while row is not None:
            print(row)
            row = cur.fetchone()
 
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
def main():
    print('Select which query you want to run: ')
    print('1 : TAG LIKED BY USER FOR FUTURE SUGGESTED POSTS')
    print('2 : LIST OF LOCATION WISE POSTS FOR ALL VISIBLE POSTS')
    print('3 : LIST OF COMMON FOLLOWERS WHO FOLLOWS BOTH USERS ')
    print('4 : TOP TRENDING TAGS')
    print('5 : AVAILABLE STORIES FOR USER')
    print('6 : LIST OF TOP REPLIED HASHTAG ON STORY FOR A USER')
    print('7 : LIST OF TOP REPLIED HASHTAG ON POSTS')
    print('8 : LIST OF TOP USERS PAIR BASED ON AVERAGE MESSAGES PER DAY')
    print('9 : FOLLOW SUGGESTION FOR A USER')
    print('10 : POST LIKED LIST WITH COUNT FOR A USER')
   
    
    value = int(input("enter"))
    print(value)
    
    if (value==1):
            q1()
    elif (value==2):
            q2()
    elif (value==3):
            q3()    
    
    elif (value==4):
            q4()

    elif (value==5):
            q5()

    elif (value==6):
            q6()

    elif (value==7):
            q7()

    elif (value==8):
            q8()

    elif (value==9):
            q9()
    elif (value==10):
            q10()
    
        
          
if __name__=="__main__":
    main()
