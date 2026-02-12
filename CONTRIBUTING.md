# 🤝 CONTRIBUTING TO ARES-X
First off, thank you for considering contributing to ARES-X! It’s people like you who make this industrial framework more powerful for everyone.

To maintain the **Industrial Grade** of this project, please follow these guidelines.

---

## 🛠️ HOW CAN YOU CONTRIBUTE?

### 1. Reporting Bugs 🐛
If you find a module that isn't working (e.g., a Scanner error or a broken Payload link):
- Open an **Issue** on the GitHub repository.
- Describe the error and include your **Termux/OS version**.
- Attach the relevant lines from `logs/audit.log` (remove private IPs first).

### 2. Suggesting New Modules 💡
ARES-X is built on a **35-file modular architecture**. If you want to add a new tool:
- Ensure the logic is placed in the `core/` subfolders.
- The module must be "Click-to-Trigger" compatible with the Web UI.
- Use the `AresExecutor` class for all terminal commands.

### 3. Improving Documentation 📖
If the `help.py` file or `README.md` is confusing, feel free to submit a PR (Pull Request) with clearer instructions for beginners.

---

## 🚀 PULL REQUEST PROCESS

1.  **Fork the Repo:** Create your own copy of ARES-X.
2.  **Create a Branch:** Name it something clear like `feat-new-scanner` or `fix-payload-bug`.
3.  **Run the Fix Script:** Before submitting, run `bash scripts/fix_env.sh` to ensure your code doesn't break the environment.
4.  **Submit PR:** Describe exactly what your change does and which of the 35 files were modified.

---

## ⚖️ CODE STANDARDS
*   **Keep it Modular:** Do not put all your code in `run.py`. Use the folder structure.
*   **Math-Driven:** Where possible, include "Math Level" calculations (Entropy/Probability) for new exploits.
*   **Silent & Stealthy:** Modules should default to stealthy modes to maintain the "Industrial" standard.

---

## 📜 ETHICAL CODE OF CONDUCT
By contributing to ARES-X, you agree that:
*   Your code will **not** be used for illegal activities.
*   You will not include any malicious "backdoors" in your contributions.
*   You respect the privacy and security of all users.

**Thank you for helping us build the future of automated security!**
