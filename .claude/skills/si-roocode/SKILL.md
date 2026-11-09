---
name: si-roocode
description: Scaffold .roomodes Boomerang multi-agent modes, .roorules coding standards, and 32k Flash-Attention Ollama configs for Roo Code in VS Code.
---

# SI-RooCode Skill

1. Run `python si_roocode_init.py --target .` in any workspace root to generate `.roomodes` and `.roorules`.
2. Run `ollama_flash_32k.bat` to enable `OLLAMA_FLASH_ATTENTION=1` and `OLLAMA_KV_CACHE_TYPE=q8_0` (cuts 32k VRAM usage by 50%).
3. Start tasks in **Chief Orchestrator** mode so large features are delegated into isolated Boomerang subtasks.
