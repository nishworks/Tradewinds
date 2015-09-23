# Run tox to create virtual environment and install packages
tox
# Activate virtual environment for this session
# You have to run source activate again after this script
source activate
# Create docs
echo "Using python -  $(which python)"
cd docs
make html
# cd to project root
cd ..
# Open docs
./open_docs.sh
