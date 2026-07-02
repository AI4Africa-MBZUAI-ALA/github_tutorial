# AI 4 Africa Workshop Starter Repo

I am Nico

<p align="center">
  <a href="https://github.com/AI4Africa-MBZUAI-ALA/github_tutorial/fork">
    <img src="https://img.shields.io/badge/Fork%20this%20repo-Start%20here-brightgreen?style=for-the-badge" alt="Fork this repo" />
  </a>
</p>

🚀 Welcome to the starter repo for the AI 4 Africa workshop.

This repository is designed for beginners. It teaches collaboration first and
machine learning second.

The workshop theme is aligned with the AI for Africa Bootcamp 2026 vision:
AI for sustainability and agriculture in Africa. The project uses a **fully
synthetic, controlled story** so every group works from the same starting point
without needing any external dataset.

## 🌍 Project Story

Students will build a tiny pipeline for a fictional **school garden / community
farm helper** app.

The goal is to predict whether a garden plot needs:

- `low` water
- `medium` water
- `high` water

The input features stay simple and relatable:

- weather
- temperature
- soil moisture
- rainfall
- crop type
- day of week

That makes the project easy to understand while still feeling real.

## 🤝 How The GitHub Workflow Works

1. Every student creates their own GitHub account.
2. One person per group forks this repository.
3. That person adds the other group members as collaborators to the fork.
4. Each person owns one file and builds one step of the pipeline.
5. If a group has fewer people, whoever finishes early can start the next file.

This is the collaboration pattern we want students to practice:

- one fork per group
- one owner per file
- one shared pipeline at the end

## 🧩 Repo Structure

The workshop files live in `to_complete/` and are numbered so students can
identify them quickly.

- `to_complete/01_data_fetch.py` - create or load the synthetic raw records
- `to_complete/02_preprocess.py` - clean the records and split them into train/test sets
- `to_complete/03_train.py` - train a simple model
- `to_complete/04_evaluate.py` - score the model and create metrics
- `to_complete/05_visualize.py` - build plots and save them to disk
- `to_complete/06_streamlit_app.py` - prepare the interactive dashboard payload

`main.py` connects everything and reports which step is missing, stubbed, or
broken.

## ✅ Rules For The Files

- Keep the function name exactly as written in the file.
- Keep the input type and output shape exactly as documented.
- Do not change the data contract between files.
- If the step is not finished yet, leave the `NotImplementedError` in place.
- Start small. Make the simplest version work first.

## 🛠️ Setup

Before coding, every group should create a virtual environment.

Why this matters:

- it keeps the workshop tools separate from your computer’s global Python
- it makes the project easier to share and reproduce
- it helps everyone use the same package versions

Create and activate a virtual environment with `venv`.

Mac or Linux:

```bash
python -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```

If your terminal uses a different shell, use the equivalent activation command
for that shell.

Every time you add a package, update `requirements.txt`.

Why this matters:

- `requirements.txt` is the shopping list for the project
- it tells other people what packages they need to install
- it helps the forked repos stay in sync

Example:

```bash
pip install pandas scikit-learn matplotlib streamlit
pip freeze > requirements.txt
```

At minimum, keep `requirements.txt` up to date whenever the code needs a new
package.

## 🔁 Suggested Group Flow

If the group has 6 people:

1. One person builds `to_complete/01_data_fetch.py`
2. One person builds `to_complete/02_preprocess.py`
3. One person builds `to_complete/03_train.py`
4. One person builds `to_complete/04_evaluate.py`
5. One person builds `to_complete/05_visualize.py`
6. One person builds `to_complete/06_streamlit_app.py`

If the group has 4 people:

- build the first 4 files first
- once someone finishes, they can help with visualization or Streamlit

## 🧪 Running The Demo

Once the files are implemented, run:

```bash
python main.py
```

If a step is still missing, `main.py` will tell you which one.

## 🧠 Why This Works For Beginners

The pipeline feels like a relay race:

- fetch the raw story
- clean it up
- train a model
- check whether it works
- turn results into pictures
- show it in a dashboard

That helps students see how teamwork turns small pieces into one complete AI
system.

## 👥 Workshop Inspiration

This starter is inspired by the AI for Africa Bootcamp 2026 and its mission to
connect AI with sustainability and agriculture in Africa.

## 🤝 Partners

<p align="center">
  <img src="assets/mbzuai-brand-logo.svg" alt="MBZUAI logo" height="80" />
  <img src="assets/ala-logo-horizontal.png" alt="African Leadership Academy logo" height="80" />
</p>

<p align="center">
  <strong>MBZUAI</strong> · <strong>African Leadership Academy</strong>
</p>

## 🔗 Official Site

- https://ai4africamp.com/
