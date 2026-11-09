import json
import tempfile
import unittest
from pathlib import Path
import si_roocode_init as m


class TestSiRooCode(unittest.TestCase):
    def test_roomodes_has_3_modes(self):
        cfg = m.build_roomodes_config()
        self.assertEqual(len(cfg["customModes"]), 3)
        slugs = [c["slug"] for c in cfg["customModes"]]
        self.assertIn("si-orchestrator", slugs)

    def test_ollama_bat_enables_flash_attention_and_q8(self):
        bat = m.build_ollama_flash_bat()
        self.assertIn("OLLAMA_FLASH_ATTENTION=1", bat)
        self.assertIn("OLLAMA_KV_CACHE_TYPE=q8_0", bat)

    def test_scaffold_workspace_creates_files(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            m.scaffold_workspace(p)
            self.assertTrue((p / ".roomodes").exists())
            self.assertTrue((p / ".roorules").exists())
            self.assertTrue((p / "ollama_flash_32k.bat").exists())
            parsed = json.loads((p / ".roomodes").read_text(encoding="utf-8"))
            self.assertEqual(len(parsed["customModes"]), 3)


if __name__ == "__main__":
    unittest.main()
