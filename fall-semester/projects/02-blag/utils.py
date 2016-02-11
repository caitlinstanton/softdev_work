import hashlib, datetime
from pymongo import MongoClient

#Liam is pulling this

# All methods should be rewritten using mongo instead of SQLite

#----------------------------------Writing--------------------------------

def writePost(title, txt, idu):
    connection = MongoClient()
    db = connection['data']
    res = db.posts.find()
    PIDs = []
    for doc in res:
        PIDs.append(doc['pid'])
    if len(PIDs) == 0:
        idp = 0
    else:
        idp = max(PIDs)
    db.posts.insert({'title':title, 'content':txt, 'uid':idu, 'pid':idp+1, 'time':str(datetime.datetime.now())[:-7]})
    return idp + 1
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT MAX(pid) FROM posts"
    idp = cur.execute(q).fetchone()[0]
    if idp == None:
        idp = 0
    print idp+1
    q = "INSERT INTO posts(title,content,uid,pid) VALUES(?,?,?,?)"
    cur.execute(q,(title,txt,idu,idp+1))
    conn.commit()
    return idp + 1
    """

def writeComment(txt, idu, idp):
    connection = MongoClient()
    db = connection['data']
    res = db.comments.find()
    CIDs = []
    for doc in res:
        CIDs.append(doc['cid'])
    if len(CIDs) == 0:
        idc = 0
    else:
        idc = max(CIDs)
    db.comments.insert({'content':txt, 'cid':idc+1, 'pid':idp, 'uid':idu, 'time':str(datetime.datetime.now())[:-7]})
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT MAX(cid) FROM comments"
    idc = cur.execute(q).fetchone()[0]
    if idc == None:
        idc = 0
    print idc+1
    q = "INSERT INTO comments(content,cid,pid,uid) VALUES(?,?,?,?)"
    cur.execute(q,(txt,idc+1,idp,idu))
    conn.commit()
    """

def writeProfile(idu, filename, age, color):
    connection = MongoClient()
    db = connection['data']
    db.users.update_one({'id':idu}, {'$set': {'age':age, 'color':color, 'filename':filename}})
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "UPDATE users SET age = ?, color = ?, filename = ? WHERE id = ?"
    cur.execute(q,(age,color,filename,idu))
    conn.commit()
    """
    
#----------------------------------Deleting-------------------------------

def deleteComment(idc):
    connection = MongoClient()
    db = connection['data']
    deleteCommentH(idc)
    db.comments.update_many({'cid':{'$gt':idc}}, {'$inc':{'cid':-1}})
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    deleteCommentH(idc)
    q = "UPDATE comments SET cid = cid-1 WHERE cid > %d"
    cur.execute(q%idc)    
    conn.commit()
    """

def deleteCommentH(idc):
    connection = MongoClient()
    db = connection['data']
    db.comments.delete_one({'cid':idc})
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "DELETE FROM comments WHERE comments.cid = %d"
    cur.execute(q%idc)
    conn.commit()
    """

def deletePost(idp):
    connection = MongoClient()
    db = connection['data']
    res = db.comments.find({'pid':idp})
    for comment in res:
        deleteCommentH(comment['cid'])
    allComments = db.comments.find()
    numComments = db.comments.count()
    i = 0
    while i < numComments:
        db.comments.update_many({'cid':allComments[i]['cid']}, {'$set':{'cid':i+1}})
        i += 1
    db.posts.delete_one({'pid':idp})
    db.posts.update_many({'pid':{'$gt':idp}}, {'$inc':{'pid':-1}})
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT comments.cid FROM comments WHERE comments.pid = %d"
    bad = cur.execute(q%idp).fetchall()
    for comment in bad:
        deleteCommentH(comment[0])
    q = "UPDATE comments SET cid = rowid"
    cur.execute(q)
    q = "DELETE FROM posts WHERE posts.pid = %d"
    cur.execute(q%idp)
    q = "UPDATE posts SET pid = pid-1 WHERE pid > %d"
    cur.execute(q%idp)    
    conn.commit()
    """

#----------------------------------Getting--------------------------------

def getCommentsOnPost(idp):
    connection = MongoClient()
    db = connection['data']
    res = db.comments.find({'pid':idp})
    all_rows = []
    for doc in res:
        userID = doc['uid']
        resUser = db.users.find({'id':userID})
        row = [doc['content'], doc['time'], resUser[0]['name'], doc['cid'], resUser[0]['filename']]
        all_rows.append(row)
    return all_rows
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT comments.content,datetime(comments.time,'localtime'),users.name,comments.cid,users.filename FROM comments, users WHERE comments.pid = %d AND users.id = comments.uid"
    result = cur.execute(q%idp).fetchall()
    conn.commit()
    return result
    """

def getComment(cid):
    connection = MongoClient()
    db = connection['data']
    res = db.comments.find({'cid':cid})
    userID = res[0]['uid']
    userRes = db.users.find({'id':userID})
    username = userRes[0]['name']
    commentInfo = [res[0]['content'], res[0]['cid'], res[0]['pid'], res[0]['uid'], res[0]['time'], username]
    return commentInfo
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT comments.*,users.name FROM comments, users WHERE comments.cid = %d AND users.id = comments.uid"
    result = cur.execute(q%cid).fetchone()
    return result
    """

def getUserPosts(idu):
    connection = MongoClient()
    db = connection['data']
    res = db.posts.find({'uid':idu})
    posts = []
    for doc in res:
        posts.append(doc)
    return posts
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT * FROM posts WHERE posts.uid = %d"
    result = cur.execute(q%idu).fetchall()
    conn.commit()
    return result
    """

def getPost(idp):
    connection = MongoClient()
    db = connection['data']
    res = db.posts.find({'pid':idp})
    userID = res[0]['uid']
    userRes = db.users.find({'id':userID})
    username = userRes[0]['name']
    userfilename = userRes[0]['filename']
    postInfo = [res[0]['title'], res[0]['content'], res[0]['uid'], res[0]['pid'], res[0]['time'], username, userfilename]
    return postInfo
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT posts.*,users.name,users.filename FROM posts,users WHERE posts.pid = %d AND posts.uid = users.id"
    result = cur.execute(q%idp).fetchone()
    conn.commit()
    return result
    """

def getAllPosts():
    connection = MongoClient()
    db = connection['data']
    res = db.posts.find().sort('pid', -1)
    all_rows = []
    for doc in res:
        userID = doc['uid']
        resUser = db.users.find({'id':userID})
        row = [doc['content'], doc['pid'], doc['uid'], resUser[0]['name'], doc['title'], doc['time'], resUser[0]['filename']]
        all_rows.append(row)
    return all_rows
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT posts.content,posts.pid,posts.uid,users.name,posts.title,datetime(posts.time,'localtime'),users.filename FROM posts, users WHERE users.id = posts.uid ORDER BY posts.pid DESC"
    cur.execute(q)
    all_rows = cur.fetchall()
    print all_rows
    conn.commit()
    return all_rows
    """

def getAllUsers():
    connection = MongoClient()
    db = connection['data']
    res = db.users.find()
    all_rows = []
    for doc in res:
        all_rows.append([doc['name']])
    return all_rows
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = "SELECT users.name FROM users"
    cur.execute(q)
    all_rows = cur.fetchall()
    #print all_rows
    conn.commit()
    return all_rows
    """

def getProfile(uid):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'id':uid})
    profile = [res[0]['name'], res[0]['filename'], res[0]['age'], res[0]['color']]
    return profile
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = 'SELECT name,filename,age,color FROM users WHERE users.id = %d'
    cur.execute(q%uid)
    row = cur.fetchone()
    conn.commit()
    return row
    """

#----------------------------------Log In---------------------------------
    
def encrypt(word):
    hashp = hashlib.md5()
    hashp.update(word)
    return hashp.hexdigest()

def authenticate(username,password):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':username})
    for doc in res:
        if encrypt(password) == doc['password']:
            return True
    return False
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = 'SELECT users.password FROM users WHERE users.name = "%s"'
    result = cur.execute(q%username)
    for r in result:
        if(encrypt(password) == r[0]):
            return True
    conn.commit()
    return False
    """

def getUserId(name):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'name':name})
    num = db.users.count({'name':name})
    if num == 0:
        return None
    else:
        return res[0]['id']
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = 'SELECT users.id FROM users WHERE users.name = "%s"'
    result = cur.execute(q%name).fetchone()
    conn.commit()
    if result==None:
        return None
    return result[0]
    """

def getUserName(uid):
    connection = MongoClient()
    db = connection['data']
    res = db.users.find({'id':uid})
    return res[0]['name']
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = 'SELECT users.name FROM users WHERE users.id = %d'
    result = cur.execute(q%uid).fetchone()
    conn.commit()
    return result[0]
    """

def addUser(username,password):
    connection = MongoClient()
    db = connection['data']
    num = db.users.count({'name':username})
    if num == 0:
        users = db.users.find()
        IDs = []
        for doc in users:
            IDs.append(doc['id'])
        if len(IDs) == 0:
            uid = 0
        else:
            uid = max(IDs)
        db.users.insert({'name':username, 'password':encrypt(password), 'id': uid+1, 'picid':-1, 'age':-1, 'color':'', 'filename':''})
        return True
    return False
    """
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    q = 'SELECT users.name FROM users WHERE users.name = ?'
    result = cur.execute(q,(username,)).fetchone()
    if result == None:
        q = 'SELECT max(users.id) FROM users'
        uid = cur.execute(q).fetchone()[0]
        if uid==None:
            uid=0
        q = 'INSERT INTO users VALUES (?, ?, ?,-1,-1,"","")'
        cur.execute(q, (username, encrypt(password), uid+1))
        print str(uid+1)+","+username
        conn.commit()
        return True
    conn.commit()
    return False
    """
