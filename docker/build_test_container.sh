# Copy files to docker folder
cp /Users/soeren/code/googletrends/googletrends/src/functions.py \
    /Users/soeren/code/googletrends/googletrends/docker/functions.py

cp /Users/soeren/code/googletrends/googletrends/trends.py \
    /Users/soeren/code/googletrends/googletrends/docker/trends.py

# Build docker image
docker build --tag python-docker:simple .

# Test docker image
docker run \
    -v /Users/soeren/code/googletrends/googletrends/:/app \
    python-docker:simple \
    --search_term=Ukraine \
    --start_time=2016-12-13 \
    --end_time=2022-01-11 \
    --export_target=/Users/soeren/Desktop/data.csv