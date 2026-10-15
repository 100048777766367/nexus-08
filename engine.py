import os
import sys
import json

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex.sense_intake import SenseIntakeLobe
from cortex.consensus_immune import ConsensusImmuneLobe
from cortex.mind_sandbox import MindSandboxLobe
from cortex.transmute_act import TransmuteActLobe

# Chỉ quét tự vá các cơ quan nền tảng dùng chung giữa các thế hệ
VITAL_SHARED_CELLS = [
    "cells/linguistic_cell.py",
    "cells/neuron.py",
    "cells/super_xor.py"
]

class Nexus08GrandEngine:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-08")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-07"
        
        self.lineage = [
            f"{self.owner}/nexus-07", f"{self.owner}/nexus-06",
            f"{self.owner}/nexus-05", f"{self.owner}/nexus", f"{self.owner}/genome"
        ]

        self.ensure_folders()

        # 4 ĐẠI THÙY NÃO TRỤC THẬP TỰ
        self.sense_lobe = SenseIntakeLobe(self.owner, self.lineage)
        self.consensus_lobe = ConsensusImmuneLobe()
        self.mind_lobe = MindSandboxLobe(num_cells=8)
        self.transmute_lobe = TransmuteActLobe()

        self.context = {
            "repo_name": self.repo_name,
            "owner": self.owner,
            "ancestor": self.ancestor,
            "peers": self.load_peers(),
            "current_epoch": self.load_epoch()
        }

    def ensure_folders(self):
        for d in ["cells", "cortex", "synapses", "synapses/harvested_memory"]:
            os.makedirs(d, exist_ok=True)

    def load_peers(self):
        p_file = "synapses/peers.json"
        if os.path.exists(p_file):
            try:
                with open(p_file, "r") as f: return json.load(f).get("trusted_peers", [])
            except Exception: pass
        return [
            f"{self.owner}/nexus-07", f"{self.owner}/nexus-06",
            f"{self.owner}/neuron", f"{self.owner}/seed", f"{self.owner}/motor"
        ]

    def load_epoch(self):
        s_file = "synapses/state.json"
        if os.path.exists(s_file):
            try:
                with open(s_file, "r") as f: return json.load(f).get("generation_epoch", 0) + 1
            except Exception: pass
        return 1

    def run(self):
        print("=" * 80)
        print(f"🌌 [NEXUS-08 GRAND CROSS] KHỞI ĐỘNG THẾ HỆ #{self.context['current_epoch']}")
        print(f"👑 Bậc: F8 Đại Giao Điểm Thần Kinh – Trục Thập Tự 4 Đại Thùy Não")
        print("=" * 80)

        # 1. Thùy Cảm Thụ: Tiếp nhận tri thức ngoại giới & Tự vá tế bào
        self.sense_lobe.process(self.context, VITAL_SHARED_CELLS)

        # 2. Thùy Miễn Dịch: Thu thập tín hiệu P2P, Lọc Byzantine & Hòa âm Kuramoto
        self.consensus_lobe.process(self.context)

        # 3. Thùy Tâm Thức: Đồ thị tri thức, Giả lập What-If & Siêu XOR
        self.mind_lobe.process(self.context)

        # 4. Thùy Chấp Hành: La bàn Bồ Đề, Biến hình 11 tầng, Chuyển sinh 404 & Phát sóng
        self.transmute_lobe.process(self.context)

        print("=" * 80)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F8] Đại Giao Điểm đã khúc xạ hoàn mỹ khắp 11 tầng!")
        print("=" * 80)

if __name__ == "__main__":
    node = Nexus08GrandEngine()
    node.run()
