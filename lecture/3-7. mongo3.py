from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta

# 영화 제목 '매트릭스'의 평점을 가져오기

# 딱 그 특정한 제목의 영화를 찾아야하므로 'find_one' 사용
movie_targ = db.movies.find_one({'title': '매트릭스'})
print(movie_targ['star'])

# 매트릭스의 평점과 같은 평점의 영화 제목들을 가져오기

star_targ = movie_targ['star']
movies = list(db.movies.find({'star': star_targ}))

'''
movies = list(db.movies.find({'star': movie_targ['star']}))
'''

print(len(movies))

for movie in movies:
    print(movie['title'])


# 위 영화들의 평점을 0으로 만들기
# DB를 수정할땐, update, 하나만 수정하는게 아니니까, many

db.movies.update_many({'star': star_targ}, {'$set': {'star': '0'}})
