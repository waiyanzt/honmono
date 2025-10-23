# Honmono: A Fake News Classifier

**Oregon State University AI Club - Introductory ML Project**

A machine learning project to classify news articles as real or fake using natural language processing and classification algorithms.「本物 (ほんもの、 honmono) 」means “real” or “genuine."

---

## 📋 Project Overview

This is a "get your toes wet" machine learning project focusing on binary text classification. We're working with ~20,000 news articles (split between real and fake) from Kaggle to build and evaluate various ML models.

**Learning Goals:**
- Data loading and preprocessing
- Text feature extraction (TF-IDF, word embeddings)
- Training classification models (Logistic Regression, Naive Bayes, etc.)
- Model evaluation and comparison
- Collaborative ML workflow with Git

---

## 👥 Team Members

- Wai Yan Zaw (Marcus) Tin
- Yuan Chao (Teddy) Lee
- Bryan Huang

---

## 📊 Dataset

**Source:** https://www.kaggle.com/datasets/bhavikjikadara/fake-news-detection/data

**Structure:**
- `true.csv`: Real news articles (21,417 articles)
- `fake.csv`: Fake news articles (23,481 articles)
- Combined dataset: 44,898 total articles
- **Label distribution:** 47% real, 53% fake (well-balanced ✓)

**Features (typical for this type of dataset):**
- `title`: Article headline
- `text`: Article body content 
- `subject`: News category or type of news
- `date`: Publication date

---

## ⚠️ Project Scope & Limitations

**What this project IS:**
- A learning exercise in text classification using classical ML
- Training models to detect patterns in a specific dataset (<2018 news)
- Understanding evaluation metrics and model comparison
- Practicing the complete ML workflow from data to deployment

**What this project IS NOT:**
- A production-ready fake news detector
- Generalizable to all news articles, social media, or different time periods
- A solution to misinformation (that requires continuous retraining, fact-checking, multi-modal analysis)

**Expected Performance:**
- High accuracy (~90-95%) on test data from the same dataset
- Poor generalization to news from different sources/time periods
- This demonstrates the concept of **distribution shift** - models learn patterns specific to their training data

**Key Insight:** The model learns statistical patterns in writing style and vocabulary, not "truth" or "fact-checking". It identifies articles similar to the fake news in the training set, but won't catch novel misinformation strategies.

---

## 🚀 Setup Instructions

### For NixOS Users

1. **Enter development environment:**
   ```bash
   nix-shell
   ```

2. **Download dataset manually:**
   ```bash
   # Go to https://www.kaggle.com/datasets/bhavikjikadara/fake-news-detection/data?select=true.csv
   # Click "Download" button
   # Extract the ZIP file
   # Copy true.csv and fake.csv into the data/ directory
   ```

### For Non-NixOS Users

1. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies:**
   ```bash
   pip install pandas numpy matplotlib scikit-learn jupyter
   ```

3. **Follow step 2 from NixOS instructions above**

---

## 🏃 Quick Start

### Load and Explore Data

```bash
# Make sure you're in nix-shell (NixOS) or have venv activated
python src/load_data.py
```

This will:
- Load both CSV files
- Combine and shuffle the data
- Display dataset statistics
- Show label distribution visualization

### Expected Output

```
Loading datasets...
✓ Loaded 10413 real articles
✓ Loaded 10387 fake articles
✓ Total: 20800 articles

============================================================
DATASET INFORMATION
============================================================

Shape: 20800 rows × 5 columns
Columns: ['title', 'text', 'subject', 'date', 'label']
...
```

---

## 📁 Project Structure

```
honmono/
├── shell.nix              # Nix development environment
├── README.md              # This file
├── .gitignore            # Git ignore rules
├── data/                 # Dataset directory (not committed)
│   ├── .gitkeep
│   ├── true.csv          # Real news articles
│   └── fake.csv          # Fake news articles
├── src/                  # Source code
│   └── load_data.py      # Data loading and exploration
└── notebooks/            # Jupyter notebooks for analysis
    └── .gitkeep
```

---

## 🛠️ Development Workflow

### Basic Git Workflow

```bash
# Pull latest changes
git pull origin main

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes, then stage and commit
git add .
git commit -m "Add: brief description of changes"

# Push to GitHub
git push origin feature/your-feature-name

# Create Pull Request on GitHub for team review
```

### Running Jupyter Notebooks

```bash
# Inside nix-shell or with venv activated
jupyter notebook

# Navigate to notebooks/ directory in the browser
```

---

## 📝 Next Steps

- [ ] Exploratory Data Analysis (EDA)
  - Text length distribution
  - Common words in real vs fake news
  - Subject/category analysis
  
- [ ] Text Preprocessing
  - Lowercase conversion
  - Punctuation removal
  - Tokenization
  - Stop word removal
  - Stemming/Lemmatization

- [ ] Feature Engineering
  - TF-IDF vectorization
  - Word2Vec embeddings
  - Feature selection

- [ ] Model Training
  - Baseline: Logistic Regression
  - Naive Bayes
  - Random Forest
  - (Stretch) Neural Networks

- [ ] Evaluation
  - Accuracy, Precision, Recall, F1
  - Confusion Matrix
  - Cross-validation
  - Error analysis

---

## 🧪 Testing Your Setup

Quick verification that everything works:

```python
# Run this in Python REPL
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

print("✓ All packages imported successfully!")
```

---

## 📚 Resources

- **Scikit-learn Documentation:** https://scikit-learn.org/
- **Pandas Documentation:** https://pandas.pydata.org/docs/
- **Text Classification Tutorial:** https://scikit-learn.org/stable/tutorial/text_analytics/working_with_text_data.html
- **OSU AI Club:** [Add club link if available]

---

## 🐛 Troubleshooting

### "Module not found" errors
- **NixOS:** Make sure you're inside `nix-shell`
- **Others:** Ensure virtual environment is activated

### Kaggle API not working
```bash
# Verify credentials file exists
ls -la ~/.kaggle/kaggle.json

# Should show: -rw------- (permissions 600)
```

### Data files not found
- Ensure CSV files are in `data/` directory
- Check filenames are exactly `true.csv` and `fake.csv`

---

## 📄 License

This is an educational project for OSU AI Club members.

---

## 🤝 Contributing

1. Create a feature branch
2. Make your changes
3. Test your code
4. Submit a Pull Request
5. Wait for team review

**Code Style:**
- Use type hints where possible
- Add docstrings to functions
- Keep functions focused and small

---

## 📧 Contact

For questions or issues, reach out to the team on [tinw@oregonstate.edu].

---

**Happy Learning! 🎓🤖**
