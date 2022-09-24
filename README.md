## Conda

Conda-related commands:

- Create the conda environment:
  `conda env create -f environment.yaml`

- Activate the conda environment:
  `conda activate tsa`

- Deactivate the conda environment:
  `conda deactivate`

- Update the conda environment (such as if there were changes to environment.yml in the git repository):
  `conda env update --prefix ./env --file environment.yml --prune`

- Delete the conda environment (if necessary):
  `conda env remove -n tsa`
