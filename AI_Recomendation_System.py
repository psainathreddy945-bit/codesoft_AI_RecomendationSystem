import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def load_dataset(filename):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    dataset_path = os.path.join(base_dir, filename)

    if not os.path.exists(dataset_path):
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    return pd.read_csv(dataset_path)


def get_similarity(dataframe, column_name):
    cv = CountVectorizer()
    vectors = cv.fit_transform(dataframe[column_name].fillna("").astype(str))
    return cosine_similarity(vectors)


def recommend_items(dataframe, item_column, item_name, similarity, label):
    item_name = item_name.strip().lower()
    matches = dataframe[dataframe[item_column].astype(str).str.lower() == item_name].index

    if len(matches) == 0:
        print(f"{label} not found!")
        return []

    index = matches[0]
    distances = sorted(enumerate(similarity[index]), key=lambda x: x[1], reverse=True)

    recommendations = []
    for i in distances[1:6]:
        recommendations.append(dataframe.iloc[i[0]][item_column])

    return recommendations


def main():
    movies = load_dataset("movies.csv")
    books = load_dataset("books.csv")

    movie_similarity = get_similarity(movies, "genre")
    book_similarity = get_similarity(books, "genre")

    choice = input("Do you want movie or book recommendations? ").strip().lower()

    if choice in ["movie", "movies"]:
        movie_name = input("Enter your favorite movie: ").strip()
        recommendations = recommend_items(movies, "movie", movie_name, movie_similarity, "Movie")

        if recommendations:
            print("\nRecommended Movies:")
            for title in recommendations:
                print(title)

    elif choice in ["book", "books"]:
        book_name = input("Enter your favorite book: ").strip()
        recommendations = recommend_items(books, "title", book_name, book_similarity, "Book")

        if recommendations:
            print("\nRecommended Books:")
            for title in recommendations:
                print(title)

    else:
        print("Please enter 'movie' or 'book'.")


if __name__ == "__main__":
    main()