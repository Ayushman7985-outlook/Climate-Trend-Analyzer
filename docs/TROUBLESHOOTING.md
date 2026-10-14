# Troubleshooting

| Problem | Likely reason | Solution | Prevention |
|---|---|---|---|
| `python` not recognized | Python missing from PATH | Reinstall Python and enable PATH, or use `py` on Windows | Verify `python --version` |
| Virtual environment activation blocked | PowerShell execution policy | In current terminal use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`, then activate | Use process scope rather than changing system policy |
| `ModuleNotFoundError` | Dependencies installed in another environment | Activate `.venv`, then `python -m pip install -r requirements.txt` | Use the same interpreter for pip and run commands |
| File not found | Command run outside project root | `cd` into `Climate-Trend-Analyzer` | Run commands from repository root |
| Date parsing creates missing dates | Date strings inconsistent | Inspect raw CSV and use `pd.to_datetime(..., errors='coerce')` | Keep dates in ISO format `YYYY-MM-DD` |
| Missing values remain | Entire column may be empty or malformed | Inspect `df.isna().sum()` and source data | Validate data before analysis |
| Plot window does not appear | Script saves charts using a noninteractive backend | Open PNGs in `outputs/images/` | Check the output directory |
| No anomalies seem meaningful | Contamination setting or feature scales | Explain flags as candidates; test several settings | Avoid treating flags as ground truth |
| Trend seems too strong | Synthetic warming signal or outliers | Review source, plot yearly values, and compare robust methods | Document data origin and limits |
| `pytest` not found | pytest not installed in active environment | `python -m pip install pytest` then `python -m pytest -q` | Use `python -m pytest` |
| Git says not a repository | Git not initialized or wrong directory | `git init` in the project root | Check `git status` |
| Push rejected | Remote contains an initial commit or branch mismatch | `git pull --rebase origin main`, resolve conflicts, then push | Decide whether to initialize README locally or on GitHub, not both |
