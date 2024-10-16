# Interactive Jupyter Notebooks and Automated Repair Service based on Break-It-Fix-It research

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/vquanghuy/breakdown-bifi/blob/main/Breakdown_BIFI.ipynb)

This project is the reimplementation of the Break-It-Fix-It (BIFI) unsupervised program repair method introduced in the ICML 2021 paper of the same name ([https://github.com/michiyasunaga/BIFI](https://github.com/michiyasunaga/BIFI)). My primary goals are to enhance clarity and accessibility for researchers and developers interested in unsupervised learning for code repair.

## Features

* **Jupyter Notebooks:**  The entire BIFI algorithm, including the breaker, fixer, and critic components, has been refactored into interactive Jupyter notebooks. This format facilitates a step-by-step understanding of the unsupervised learning process and encourages experimentation.
* **PyTorch/fairseq Compatibility:** The codebase has been updated to align with the **PyTorch 2.3.1** and the **fairseq 0.12.2**.

## BIFI Overview

The Break-It-Fix-It method is an innovative approach to unsupervised program repair. It consists of three main components:

* **Breaker:**  Learns to introduce realistic errors into correct code snippets.
* **Fixer:**  Trained to repair code, initially on synthetic errors and later on the breaker's more realistic errors.
* **Critic:**  Evaluates the correctness of code, guiding the iterative improvement of the breaker and fixer.

## Usage

1. **Clone the Repository:**
   ```bash
   git clone git@github.com:vquanghuy/jupyter-bifi-adaptation.git
   cd jupyter-bifi-adaptation
   ```
2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Open and Run Jupyter Notebooks:**
    * **Data Preparation:** Notebooks to prepare your unlabeled code corpus and any initial synthetic errors.
    * **BIFI Training:** Notebooks guiding you through the iterative training of the breaker and fixer components.
    * **Evaluation:** Notebooks to assess the performance of your BIFI model on various code repair tasks.

## Updates and Improvements

* **PyTorch/fairseq:** The codebase utilizes the most recent stable versions of these libraries for enhanced performance and compatibility.
* **Jupyter Notebooks:**  The notebooks provide comprehensive explanations of the BIFI algorithm and offer flexibility for experimentation.
* **Code Refactoring:**  The code has been reorganized and improved for better readability and maintainability.

## Code Fixer API

Navigate to the server folder and run command

## For debug

```bash
python app.py
```

## For production

```bash
waitress-serve --port=8080 --call app:create
```

## Acknowledgements

I extend my gratitude to Michihiro Yasunaga and Percy Liang - the authors of the BIFI paper for their pioneering work in unsupervised program repair.

```bib
@misc{yasunaga2021breakitfixitunsupervisedlearningprogram,
      title={Break-It-Fix-It: Unsupervised Learning for Program Repair}, 
      author={Michihiro Yasunaga and Percy Liang},
      year={2021},
      eprint={2106.06600},
      archivePrefix={arXiv},
      primaryClass={cs.LG},
      url={https://arxiv.org/abs/2106.06600}, 
}
```

## License

This project is licensed under the MIT License.
