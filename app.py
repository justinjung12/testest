from flask import Flask, request, redirect,jsonify
from datetime import datetime
app = Flask(__name__)


#맨 앞은 가장 처음 올라온 뉴스 뒤로 갈수록 오래된 뉴스
news = [
    {'title':'뉴스입니다','contents':'이것은 뉴스입니다','keywords':['important','sports'], 'date':'2024-02-28','time':'오후 1시 30분'},
    {'title':'뉴스1입니다','contents':'이것은 뉴스1입니다','keywords':['word'], 'date':'2024-02-28','time':'오후 1시 30분'},
]
postivecomments = [
    {'title':'뉴스입니다','text':'와 재미있다 뉴스','goodNumber':10,'badNumber':5,'id':0},
    {'title':'뉴스1입니다','text':'와 재미있다 뉴1스ㅋ','goodNumber':5,'badNumber':1,'id':1}
]                           
negativecomments = [
    {'title':'뉴스입니다','text':'와 재미없다 뉴스','goodNumber':10,'badNumber':5, 'id':0},
    {'title':'뉴스1입니다','text':'와 재미없다 뉴1스ㅋ','goodNumber':10,'badNumber':1, 'id':1}
]
#시간순으로 보여주기 방식 
@app.route('/timenews/<int:start_number>/') #start_number:어느 페이지 부터 보여줄 것인지
def showtimenews(start_number):
    result = {}
    show_news = news[start_number]
    show_news__postive_comments = []    
    show_news__negative_comments = []
    
    for i in postivecomments:
        if i['title'] == show_news['title']:
            show_news__postive_comments.append(i)

    for j in negativecomments:
        if j['title'] == show_news['title']:
            show_news__negative_comments.append(j)
    result['news'] = show_news
    result['postivecomments'] = show_news__postive_comments
    result['negativecomments'] = show_news__negative_comments
    return jsonify(result)

@app.route('/plusnumbergood/<string:Type>/',methods=['GET', 'POST']) #commant_id:댓글 id
def plusnumbergood(Type):
    if request.method == 'POST':
        if Type == 'postive':
            for i in postivecomments:
                if i['text'] == request.form['text']:
                    postivecomments[postivecomments.index(i)]['goodNumber'] += 1
                    return postivecomments
        if Type == 'negative':
            for j in negativecomments:
                if j['text'] == request.form['text']:
                    negativecomments[negativecomments.index(j)]['goodNumber'] += 1
                    return negativecomments
    

@app.route('/plusnumberbad/<int:command_id>/<string:Type>/') #commant_id:댓글 id
def plusnumberbad(command_id,Type):
    if Type == 'postive':
        for i in postivecomments:
            if i['id'] == command_id:
                postivecomments[postivecomments.index(i)]['badNumber'] += 1
                print(i) 
    elif Type == 'negative':
        for i in negativecomments:
            if i['id'] == command_id:
                negativecomments [postivecomments.index(i)]['badNumber'] += 1
                print(i)
    return 'hi'

@app.route('/addcommand/<string:Type>/',methods=['GET', 'POST']) #commant_id:댓글 id
def addcommand(Type):
    if request.method == 'POST':
        result = {}
        result['title'] = request.form['title']
        result['text'] = request.form['text']
        result['goodNumber'] = 0
        result['badNumber'] = 0
    if Type == 'postive':
        result['id'] = len(postivecomments)
        postivecomments.append(result)
        return postivecomments
    elif Type == 'negative':
        result['id'] = len(negativecomments)
        negativecomments.append(result)
        return negativecomments
    
@app.route('/admin/',methods=['GET', 'POST']) #commant_id:댓글 id
def admin():
    if request.method == 'POST':
        if request.form['password'] == 'woojiny':
            current_date = datetime.now()
            current_time = datetime.now().time()
            result = {}
            result['title'] = request.form['title']
            result['contents'] = request.form['contents']
            result['keywords'] = request.form['keywords']
            result['date'] = current_date.strftime("%Y-%m-%d")
            result['time'] = current_time.strftime("%H:%M")
            news.append(result)
            return 'success'
app.run()
