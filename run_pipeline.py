import subprocess

print("Starting N100 Financial Intelligence Platform Pipeline...")

subprocess.run(["python", "-m", "src.etl.loader"])
subprocess.run(["python", "src/etl/database.py"])
subprocess.run(["python", "src/etl/load_data.py"])
subprocess.run(["python", "src/etl/manual_review.py"])

print("Pipeline completed successfully.")
print("nifty100.db is ready for analysis.")