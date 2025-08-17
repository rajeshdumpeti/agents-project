# Agents Project

Agents Template

Industrial-grade, reusable template for building autonomous AI agents that assist with product delivery: clarification → rules → stories → tests → docs → planning. Designed to run **offline by default**, integrate with GitHub/Slack when enabled, and scale from solo-dev to team workflows.

## 🔧 Features
- **Project-agnostic:** swap `configs/<project>.yaml` to reuse across domains.
- **Role agents:** PRL (clarify) → SRA (rules) → USG (stories) → QAT (tests) → DOC (docs) → RPM (planning).
- **Artifact-first:** JSON/Markdown outputs saved under `artifacts/YYYY-MM-DD/`.
- **Schema-oriented:** stable formats for rules/stories/test plans.
- **Quality gates:** ruff, black, mypy, pytest, pre-commit, GitHub Actions CI.
- **Safe integrations:** optional GitHub Issues + Slack; no code writes to other repos.

## 🗂 Repo Structure
```
agents-project/
├─ configs/          # per-project config (e.g., upa.yaml)
├─ prompts/          # role prompts (prl_clarify.txt, sra_rules.txt, usg_storysmith.txt, qat.txt)
├─ schemas/          # (optional) JSON/YAML schemas for outputs
├─ data/             # local inputs (rule PDFs, notes)
├─ storage/          # vector DB/cache (gitignored)
├─ agents/           # agent nodes (prl.py, sra.py, usg.py, qat.py)
├─ pipelines/        # orchestration graphs (plan_graph.py)
├─ ingestion/        # pdf_to_md, embeddings, chunking (to be added next steps)
├─ integrations/     # adapters: github_issues.py, slack_notify.py (optional)
├─ tests/            # smoke tests and schema checks
├─ artifacts/        # timestamped run outputs (gitignored)
├─ docs/             # living docs (changelog, decisions, README snippets)
├─ run.py            # entry point
├─ requirements.txt  # runtime + dev deps (pinned)
├─ pyproject.toml    # ruff/black/mypy config
└─ .pre-commit-config.yaml
```

## 🧱 Prereqs
- Python **3.13** (repo targets your local runtime)
- `pip`, `venv`
- (Optional) GitHub account for CI and Issues integration

## 🚀 Quick Start
```bash
# clone your repo
git clone https://github.com/<you>/agents-project.git
cd agents-project

# create & activate venv
python3 -m venv venv
source venv/bin/activate

# install deps
pip install -r requirements.txt

# create a project config
cp configs/upa.yaml configs/myproject.yaml   # edit values inside
```

Run the skeleton pipeline:
```bash
python run.py
```

Run tests:
```bash
pytest -q
```

Enable pre-commit hooks:
```bash
pre-commit install
pre-commit run --all-files
```

## ⚙️ Configuration (`configs/<project>.yaml`)
```yaml
project_name: "Name of you Project"
modes: ["", "", ""] // write your modes here
inputs:
  rules_pdfs: []                # add local paths under ./data
outputs_dir: "./artifacts"
github:
  enabled: false                # flip true when ready
  owner: "your-github-username"
  repo: "repo-name"
  labels: ["agent", "story", "upa"]
slack:
  enabled: false
  webhook_url: "${SLACK_WEBHOOK:-}"
models:
  reasoning: "bedrock:anthropic.claude-3-5-sonnet"
  embedding: "bedrock:amazon.titan-embed-text-v2"
rag:
  chunk_size: 1200
  chunk_overlap: 150
  collection: "rules"
```

## 🔁 Workflow (high level)
1. **PRL** generates a Clarification Pack → you sync answers with PO.
2. **SRA** converts rules text into `rules.json` with stable section IDs.
3. **USG** produces INVEST stories citing rule IDs.
4. **QAT** derives minimal deterministic test steps.
5. **DOC** updates living docs (changelog/decisions).
6. **RPM** compiles sprint plan; optional GitHub Issues export.

Outputs are written to `artifacts/YYYY-MM-DD/` so you can diff runs safely.

## 🧪 Quality Gates
- **Local:** pre-commit fixes lint/format, mypy runs types, pytest runs tests.
- **CI:** `.github/workflows/ci.yml` enforces the same on PRs to `dev`/`main`.

## 🔐 Secrets
- Never commit tokens. Use a `.env` (gitignored) or GitHub Actions secrets.
- GitHub/Slack integrations noop when disabled.

## 🧭 Branching & Releases
- Branches: `main` (prod), `dev` (integration), `feat/<agent-name>` for features.
- Conventional commits: `feat:`, `fix:`, `docs:`, `test:`, `chore:`, `refactor:`.
- Tag releases when you cut stable artifacts/rules versions.

## 🗺 Roadmap (next steps)
- Ingestion: `ingestion/pdf_to_md.py` + simple embeddings store (Chroma).
- Replace stubs with LangGraph nodes + Bedrock calls.
- JSON Schema validation for `stories.json`, `rules.json` in tests.
- Integrations: GitHub Issues export and Slack notifications.
