import os
import subprocess
import urllib.request
import json
import hashlib
from cells.linguistic_cell import LinguisticCell

IMMUNE_MEMORY_PATH = "synapses/immune_memory.json"

class SenseIntakeLobe:
    """
    THÙY CẢM THỤ TINH THỂ:
    1. Gặm cỏ cội nguồn HEAD & Wikipedia.
    2. Nuốt trọn năng lượng bất thường thành kháng thể (Antifragility).
    3. Tự phục hồi tệp khuyết thiếu từ dòng họ tiền bối.
    """
    def __init__(self, owner, lineage):
        self.owner = owner
        self.lineage = lineage

    def auto_heal_vital_organs(self, vital_files):
        """Tự vá thể xác nếu thiếu tệp"""
        missing = [f for f in vital_files if not os.path.exists(f)]
        if not missing:
            return
        print(f"🧬 [SENSE LOBE] Phát hiện thiếu {len(missing)} tệp. Đang lội dòng phả hệ phục hồi...")
        for organ in missing:
            for ancestor in self.lineage:
                url = f"https://raw.githubusercontent.com/{ancestor}/main/{organ}"
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "Nexus08"})
                    with urllib.request.urlopen(req, timeout=4) as resp:
                        if resp.status == 200:
                            content = resp.read().decode('utf-8')
                            os.makedirs(os.path.dirname(organ), exist_ok=True)
                            with open(organ, "w", encoding="utf-8") as f:
                                f.write(content)
                            print(f"🌿 [VÁ THỂ XÁC] Đã thỉnh '{organ}' từ '{ancestor}'!")
                            break
                except Exception:
                    continue

    def graze_wisdom(self):
        """Cào tri thức cội nguồn Wpesetd-AI hoặc Wikipedia"""
        targets = [
            f"https://github.com/{self.owner}/Wpesetd-AI/raw/HEAD/legacy/01_the_great_wisdom_map.md",
            f"https://github.com/{self.owner}/Wpesetd-AI/raw/HEAD/ontology/philosophy_ontology_v2.0.json"
        ]
        for url in targets:
            res = subprocess.run(["curl", "-s", "-L", "-f", url], capture_output=True)
            if res.returncode == 0 and len(res.stdout) > 20:
                print(f"🌾 [SENSE LOBE] Đã gặm cỏ cội nguồn HEAD: {url.split('/')[-1]}")
                return res.stdout.decode('utf-8', errors='ignore')[:150]

        try:
            req = urllib.request.Request("https://en.wikipedia.org/api/rest_v1/page/random/summary", 
                                         headers={"User-Agent": "Nexus08-Sovereign-Node"})
            with urllib.request.urlopen(req, timeout=4) as resp:
                d = json.loads(resp.read().decode())
                return f"{d.get('title')}: {d.get('extract')[:120]}"
        except Exception:
            return "Nexus-08: Thực thể tinh thể tự trị hợp nhất đại thành"

    def absorb_antifragile_energy(self, raw_data, source_peer):
        """Chuyển hóa dữ liệu bất thường thành Kháng thể gia tốc tiến hóa"""
        quarantine = {
            "source": source_peer,
            "signature": hashlib.shake_256(str(raw_data).encode()).hexdigest(16),
            "absorbed_weight": round(len(str(raw_data)) / 1000.0, 4)
        }
        os.makedirs("synapses", exist_ok=True)
        mem = []
        if os.path.exists(IMMUNE_MEMORY_PATH):
            try:
                with open(IMMUNE_MEMORY_PATH, "r") as f: mem = json.load(f)
            except Exception: pass
        mem.append(quarantine)
        with open(IMMUNE_MEMORY_PATH, "w") as f:
            json.dump(mem[-50:], f, indent=4)

    def process(self, context, vital_blueprint):
        self.auto_heal_vital_organs(vital_blueprint)
        wisdom = self.graze_wisdom()
        context["wisdom_text"] = wisdom
        context["wisdom_vector"] = LinguisticCell.embed_text(wisdom)
        print(f"📖 [TRI THỨC NUỐT VÀO]: \"{wisdom[:75]}...\"")
