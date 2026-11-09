#!/usr/bin/env python3
"""
SI-RooCode-Kit (by SI NEWS) — Scaffolds .roomodes, .roorules, and 32k Flash-Attention Ollama scripts.
Standard library only.
"""
from __future__ import annotations
import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple


def build_roomodes_config() -> Dict[str, Any]:
    return {
        "customModes": [
            {
                "slug": "si-orchestrator",
                "name": "🚀 SI Chief Orchestrator",
                "roleDefinition": "You are the Chief Software Architect. Break complex features into isolated Boomerang subtasks and delegate to Architect, Code, and QA Debug modes.",
                "groups": ["read", "command", "mcp"],
            },
            {
                "slug": "si-cleanroom-coder",
                "name": "⚡ SI Modular Coder",
                "roleDefinition": "Write strict, typed, modular code (<200 lines per file) and verify builds in the terminal after every edit.",
                "groups": ["read", "edit", "command", "mcp"],
            },
            {
                "slug": "si-qa-verifier",
                "name": "🛡️ SI QA & Browser Verifier",
                "roleDefinition": "Run unit tests and headless browser checks; never mark a task complete until 0 errors remain.",
                "groups": ["read", "edit", "command", "browser", "mcp"],
            },
        ]
    }


def build_roorules_text() -> str:
    return (
        "# SI NEWS Studio Engineering DNA (.roorules)\n"
        "1. Keep every source file modular and under 200 lines of code.\n"
        "2. Use strict static typing (TypeScript strict / Python type annotations).\n"
        "3. Run unit tests or build verification after every multi-file edit.\n"
        "4. Preserve existing comments, docstrings, and unrelated functionality.\n"
    )


def build_ollama_flash_bat(model: str = "qwen2.5-coder:14b") -> str:
    return (
        "@echo off\n"
        "REM SI-RooCode-Kit 32k Context + KV Cache Q8 Optimizer\n"
        "set OLLAMA_FLASH_ATTENTION=1\n"
        "set OLLAMA_KV_CACHE_TYPE=q8_0\n"
        "set OLLAMA_KEEP_ALIVE=24h\n"
        f"echo Starting Ollama with Flash Attention + Q8 KV Cache for {model}...\n"
        "ollama serve\n"
    )


def scaffold_workspace(target_dir: Path) -> List[str]:
    target_dir.mkdir(parents=True, exist_ok=True)
    rm_path = target_dir / ".roomodes"
    rr_path = target_dir / ".roorules"
    bat_path = target_dir / "ollama_flash_32k.bat"

    rm_path.write_text(json.dumps(build_roomodes_config(), indent=2), encoding="utf-8")
    rr_path.write_text(build_roorules_text(), encoding="utf-8")
    bat_path.write_text(build_ollama_flash_bat(), encoding="utf-8")
    return [str(rm_path), str(rr_path), str(bat_path)]


def main(argv: List[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="SI-RooCode-Kit Scaffolder (by SI NEWS)")
    parser.add_argument("--target", type=str, default=".", help="Target workspace directory")
    args = parser.parse_args(argv)
    created = scaffold_workspace(Path(args.target))
    print(f"[OK] Scaffolded {len(created)} files into {args.target}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
