# ===============================
# import_data.py
# Sprint 1 Task: Import CSV file
# ===============================

# Import required Python libraries
import argparse      # allows command-line arguments (--input, --out)
import os            # for working with folders and file paths
import pandas as pd  # for reading and writing CSV files


def main():
    """
    Main function: handles arguments, imports a CSV,
    and saves a clean copy to the /data/raw/ folder.
    """

    # -------------------------------
    # 1. Set up command-line arguments
    # -------------------------------
    parser = argparse.ArgumentParser(
        description="Import a CSV file into data/raw/"
    )
    # --input: path to the CSV file (required)
    parser.add_argument("--input", required=True, help="Path to the CSV file to import")
    # --out: optional output folder (defaults to data/raw)
    parser.add_argument("--out", default="data/raw", help="Output folder (default: data/raw)")
    args = parser.parse_args()

    # -----------------------------------------
    # 2. Ensure the output folder exists
    # (creates it if it doesn’t, avoids errors)
    # -----------------------------------------
    os.makedirs(args.out, exist_ok=True)

    # -----------------------------------------
    # 3. Try to read the CSV file using pandas
    # Includes error handling for common problems
    # -----------------------------------------
    try:
        df = pd.read_csv(args.input)  # load CSV into a DataFrame
    except FileNotFoundError:
        print(f"❌ ERROR: File not found: {args.input}")
        return
    except pd.errors.EmptyDataError:
        print(f"❌ ERROR: File is empty: {args.input}")
        return
    except Exception as e:
        print(f"❌ ERROR reading CSV: {e}")
        return

    # -----------------------------------------
    # 4. Save a clean copy into the output folder
    # Keeps the same filename, ensures no index column
    # -----------------------------------------
    out_path = os.path.join(args.out, os.path.basename(args.input))
    df.to_csv(out_path, index=False)

    # -----------------------------------------
    # 5. Confirm success to the user
    # -----------------------------------------
    print(f"✅ Imported {args.input} → {out_path}")


# ------------------------------------------------
# Run the script only if executed directly
# (prevents it running when imported in tests)
# ------------------------------------------------
if __name__ == "__main__":
    main()
