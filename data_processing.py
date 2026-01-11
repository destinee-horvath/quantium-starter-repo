import pandas as pd
import os 

def load_and_process(file_path: str):
    """
    Load a CSV file, filter for pink morsels sales,
    calculate total sales, and return required fields.
    """
    # Read CSV file into DataFrame
    df = pd.read_csv(file_path)
    
    # Keep rows where the product is "pink morsel" (case insensitive)
    df["product"] = df["product"].astype(str).str.strip().str.lower()
    df = df[df["product"] == "pink morsel"].copy()

    # Remove $ sign from price and convert to float 
    df["price"] = df["price"].str.replace("$", "", regex=False).astype(float)

    # Create 'sales' column as quantity * price
    df["sales"] = df["quantity"] * df["price"]

    # Keep the required columns for final output
    df = df[["sales", "date", "region"]]

    return df


# List to store processed DataFrames from each CSV
all_dfs = []

# Process each CSV individually until no more files are found
i = 0
while True:  
    filename = f"data/daily_sales_data_{i}.csv"
    try:
        with open(filename, 'r'):
            all_dfs.append(load_and_process(filename))
            print(f"Processed {filename}")

    except FileNotFoundError:
        break
    i += 1

# Continue if at least one file was successfully processed
if all_dfs:
    # Concatenate all processed DataFrames into a single DataFrame
    final_df = pd.concat(all_dfs, ignore_index=True)

    # Write combined data to a single CSV 
    os.makedirs("processed_data", exist_ok=True)
    final_df.to_csv("processed_data/pink_morsels_sales.csv", index=False)
    print("Wrote processed_data/pink_morsels_sales.csv")