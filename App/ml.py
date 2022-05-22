import pandas as pd
from sklearn.feature_extraction.text  import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from .models import Book

def combined_features(row):
    return row['author']+" "+ row['description']

def get_id_from_inside(df,index):
    return df[df.index == index]["id"].values[0]

def get_index_from_id(df,id):
    return df[df.id == id].index.values[0]

def get_recommendation_for_book(book_id):
    df = pd.DataFrame(list(Book.objects.all().values()))
    features = ['description','author']
    for feature in features:
        df[feature] = df[feature].fillna('')

    df['combined_features'] = df.apply(combined_features,axis =1)

    cv = CountVectorizer()
    count_matrix = cv.fit_transform(df["combined_features"])
    cosine_sim = cosine_similarity(count_matrix)
    id = get_index_from_id(df,book_id)
    similar_books = list(enumerate(cosine_sim[id]))

    sorted_similar_books = sorted(
        similar_books, key = lambda x: x[1], reverse=True)
         
    i =0
    b_ids =[]
    for book in sorted_similar_books:
        i = i+1
        b_ids.append(get_id_from_inside(df,book[0]))

        if i> 15:
            break
    return b_ids