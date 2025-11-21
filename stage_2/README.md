# 🔬 Single-Cell RNA-seq Analysis Readme: Bone Marrow Dataset

This repository contains a Jupyter Notebook (github.py) detailing the quality control, preprocessing, clustering, and initial annotation of a single-cell RNA sequencing (scRNA-seq) dataset initially labeled as "bone marrow." The analysis was performed primarily using the Scanpy and Decoupler Python packages.

# 📝 What I Did

I analyzed a single-cell RNA sequencing dataset (bone_marrow.h5ad) using the Scanpy pipeline, followed by advanced cell type annotation using Decoupler.

The steps performed in the analysis notebook include:

Quality Control (QC): Filtered out cells with low gene counts, high mitochondrial percentage (MT < 2%), and high ribosomal percentage (RIBO < 10%). 2. Doublet Detection: Used sc.pp.scrublet to identify and mark potential doublets (two cells mistakenly captured as one).

Normalization and Feature Selection: Normalized total counts, log-transformed the data, and identified the top 2,000 highly variable genes (HVGs).

Dimensionality Reduction: Applied Principal Component Analysis (PCA) and UMAP (Uniform Manifold Approximation and Projection) for visualization.

Clustering: Used the Leiden algorithm at a resolution of 0.5 (leiden_res0_5) to define distinct cell clusters (putative cell types).

Cell Annotation:

- Mapped ENSEMBL gene IDs to gene symbols using an external database.

- Leveraged Decoupler with the PanglaoDB marker gene set to infer cell-type activity using the ULM (Universal Lasso Method) algorithm.

- Annotated the clusters based on the highest inferred cell-type activity score.

- Marker Visualization: Visualized canonical marker gene expression across the annotated clusters using Dot Plots, Violin Plots, and Heatmaps.

# 🔍 What I Found

The initial analysis suggests that the given dataset may not accurately represent a typical bone marrow sample.

Cell Type Imbalance: The automated annotation using Decoupler primarily identified mature hematopoietic cells (e.g., T cells, B cells, Monocytes, Neutrophils, Plasma cells) with a notable absence of the progenitor populations (hematopoietic stem cells, blasts, early myeloid/lymphoid precursors) that are the defining characteristic of healthy bone marrow.

Likely Source: The transcriptional profile is more indicative of a collection of circulating leukocytes—a profile typical of peripheral blood—or bone marrow that is severely perturbed (e.g., diseased or mobilized).

Next Step: Further manual validation of progenitor markers is recommended, but the current data strongly suggests the sample source or composition needs re-evaluation.

# 💻 How to Run the Code

This code is designed to be run in a standard Python environment that supports Jupyter Notebooks.

Prerequisites: Ensure you have the following packages installed:
 
```
pip install scanpy anndata decoupler pandas seaborn
```

Environment: Open the github.py file in a Jupyter Notebook environment (e.g., Jupyter Lab, VS Code, or Google Colab).

Data File: Ensure the required scRNA-seq data file, bone_marrow.h5ad, is located in the same directory as the notebook.

Execution: Run the cells sequentially from top to bottom. The notebook will download necessary gene mapping information and generate UMAP plots and visualization results (e.g., _cell_type_clustering.svg).

# What cell types did you identify?

Neutrophils - white blood cells that conducts phagocytosis.
B cells memory - specialized lymphocytes generated after the immune system's first encounter with a specific antigen. They reproduce highly specific secondary immune response upon re-exposure to the same antigen.
Platelets - important to stop bleeding by forming blood clots.
Nuocytes - act as first responders in a specific kind of immune defense called Type 2 immunity.
T cells - provide cell-mediated immunity by directly attack infected or cancerous cells and help regulate the overall immune response.
Plasma cells - specialised cells that produce antibodies.
Gamma delta T cells - unique and relatively small subset of T lymphocytes that operate at the intersection of the innate and adaptive immune systems, making them highly versatile first responders.
Monocytes - critical part of the innate immune system. They serve as the body's largest circulating defense cells, acting as sentinels, garbage collectors, and precursors to more specialized tissue-based immune cells.

# Is the tissue source really bone marrow?

No. The tissue is may be peripheral blood. There are a lot of hematologic cells. It is not bone marrow because no progenitor cells such as progenitor myeloids or lymphoids. There are many mature hematologic cells such as plasma cells which indicate that these cells are collection of cells that have mature out from the bone marrow.

# Based on the relative abundance of cell types, is the patient healthy or infected?

I would assume the patient in infected with a pathogen. Based on the immune cells, there are a large concentration of cells from the addaptive immune system including neutrophils, T, and B-cells which may suggest the patient has been sick for quite somewhile.
