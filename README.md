# 🎬📚 Movie & Book Recommendation System

A simple **content-based recommendation system** built with **Python** and **Scikit-learn**. The application recommends movies or books based on their **genre similarity** using the **CountVectorizer** and **Cosine Similarity** algorithms.

---

## 🚀 Features

- Recommend similar movies based on genre
- Recommend similar books based on genre
- Uses Content-Based Filtering
- Fast and lightweight
- Beginner-friendly project
- Command-line interface

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Scikit-learn
- CountVectorizer
- Cosine Similarity

---

## 📂 Project Structure

```
Recommendation-System/
│
├── main.py
├── movies.csv
├── books.csv
├── requirements.txt
└── README.md
```

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/recommendation-system.git
```

### 2. Navigate to the project directory

```bash
cd recommendation-system
```

### 3. Install the required libraries

```bash
pip install -r requirements.txt
```

Or install them manually:

```bash
pip install pandas scikit-learn
```

---

## ▶️ How to Run

Run the program using:

```bash
python main.py
```

---

## 🎮 Usage

When you run the program, choose whether you want movie or book recommendations.

Example:

```
Do you want movie or book recommendations?
movie

Enter your favorite movie:
Inception

Recommended Movies:
Interstellar
The Matrix
Shutter Island
The Prestige
Tenet
```

Or

```
Do you want movie or book recommendations?
book

Enter your favorite book:
Harry Potter

Recommended Books:
The Hobbit
Percy Jackson
The Chronicles of Narnia
The Hunger Games
The Maze Runner
```

---

## 🧠 How It Works

The recommendation system follows these steps:

1. Loads the movie and book datasets from CSV files.
2. Converts the **genre** column into numerical vectors using **CountVectorizer**.
3. Computes similarity scores using **Cosine Similarity**.
4. Finds the selected movie or book in the dataset.
5. Returns the five most similar recommendations based on genre.

This is an example of a **Content-Based Filtering** recommendation system.

---

## 📊 Algorithm Used

### CountVectorizer
Converts text data (genres) into numerical feature vectors.

### Cosine Similarity
Measures how similar two items are based on the angle between their feature vectors.

Similarity Score:

- **1.0** → Exactly similar
- **0.0** → Completely different

---

## 📁 Dataset Format

### movies.csv

| movie | genre |
|--------|-------|
| Inception | Sci-Fi Action |
| Interstellar | Sci-Fi Adventure |

### books.csv

| title | genre |
|-------|-------|
| Harry Potter | Fantasy Adventure |
| Percy Jackson | Fantasy Adventure |

---

## 📈 Future Improvements

- Recommend based on multiple features (genre, cast, author, rating)
- Add movie posters
- Build a GUI using Tkinter
- Develop a web application using Flask or Streamlit
- Add user ratings for personalized recommendations
- Use TF-IDF Vectorizer for improved accuracy

---

## 🎯 Learning Outcomes

This project helps you understand:

- Content-Based Recommendation Systems
- Natural Language Processing (NLP) basics
- Feature extraction using CountVectorizer
- Cosine Similarity
- Data manipulation with Pandas
- Working with CSV datasets
- Python programming

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push the branch.
5. Open a Pull Request.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you found this project useful, please consider giving it a **⭐ Star** on GitHub.
