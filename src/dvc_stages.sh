dvc stage add -n data-processing \
    -d src/data/make_dataset.py \
    -d data/raw/tripadvisor_hotel_reviews.csv \
    -o data/processed/train.csv \
    -o data/processed/test.csv \
    python3 src/data/make_dataset.py
