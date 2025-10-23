"""
Load fake news dataset from Kaggle.
This script loads true.csv and fake.csv, combines them with labels,
and provides basic exploratory analysis.
"""
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

plt.style.use("ggplot")


def load_fake_news_data(data_dir: str = "data") -> pd.DataFrame:
    """
    Load and combine true and fake news datasets.
    
    Args:
        data_dir: Directory containing true.csv and fake.csv
        
    Returns:
        Combined DataFrame with 'label' column (1=real, 0=fake)
    """
    data_path = Path(data_dir)
    
    # Load datasets
    print("Loading datasets...")
    true_df = pd.read_csv(data_path / "true.csv")
    fake_df = pd.read_csv(data_path / "fake.csv")
    
    # Add labels
    true_df['label'] = 1  # Real news
    fake_df['label'] = 0  # Fake news
    
    # Combine
    df = pd.concat([true_df, fake_df], ignore_index=True)
    
    # Shuffle
    df = df.sample(frac=1, random_state=42).reset_index(drop=True)
    
    print(f"✓ Loaded {len(true_df)} real articles")
    print(f"✓ Loaded {len(fake_df)} fake articles")
    print(f"✓ Total: {len(df)} articles\n")
    
    return df


def print_dataset_info(df: pd.DataFrame) -> None:
    """Print comprehensive dataset information."""
    print("=" * 60)
    print("DATASET INFORMATION")
    print("=" * 60)
    
    print(f"\nShape: {df.shape[0]} rows × {df.shape[1]} columns")
    print(f"\nColumns: {df.columns.tolist()}")
    
    print("\n" + "-" * 60)
    print("First 3 rows:")
    print("-" * 60)
    print(df.head(3))
    
    print("\n" + "-" * 60)
    print("Data types:")
    print("-" * 60)
    print(df.dtypes)
    
    print("\n" + "-" * 60)
    print("Missing values:")
    print("-" * 60)
    missing = df.isnull().sum()
    print(missing[missing > 0] if missing.sum() > 0 else "No missing values")
    
    print("\n" + "-" * 60)
    print("Label distribution:")
    print("-" * 60)
    print(df['label'].value_counts().sort_index())
    print(f"\nBalance: {df['label'].value_counts(normalize=True).values}")


def plot_distribution(df: pd.DataFrame) -> None:
    """Plot the distribution of real vs fake news."""
    label_counts = df['label'].value_counts().sort_index()
    
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(['Fake News', 'Real News'], label_counts.values, 
                  color=['#e74c3c', '#2ecc71'], alpha=0.8, edgecolor='black')
    
    ax.set_title('Real vs Fake News Distribution', fontsize=16, fontweight='bold')
    ax.set_ylabel('Count', fontsize=12)
    ax.set_xlabel('Article Type', fontsize=12)
    
    # Add value labels on bars
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(height):,}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.tight_layout()
    plt.show()


def main() -> None:
    """Main execution function."""
    try:
        # Load data
        df = load_fake_news_data()
        
        # Display information
        print_dataset_info(df)
        
        # Plot distribution
        print("\nGenerating visualization...")
        plot_distribution(df)
        
    except FileNotFoundError as e:
        print(f"\n❌ Error: Could not find data files!")
        print(f"   {e}")
        print("\nMake sure you've downloaded the dataset:")
        print("   1. Set up Kaggle API credentials")
        print("   2. Run: kaggle datasets download -d <dataset-name>")
        print("   3. Extract files to data/ directory")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")


if __name__ == "__main__":
    main()
