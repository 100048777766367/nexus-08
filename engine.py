import os
import sys
import json

# Thêm đường dẫn hiện tại vào sys.path để import nội bộ mượt mà
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from cortex.sense_intake import SenseIntakeLobe
from cortex.consensus_immune import ConsensusImmuneLobe
from cortex.mind_sandbox import MindSandboxLobe
from cortex.transmute_act import TransmuteActLobe

VITAL_BLUEPRINT = [
    "cells/linguistic_cell.py",
    "cells/neuron.py",
    "cells/super_xor.py",
    "cortex/sense_intake.py",
    "cortex/consensus_immune.py",
    "cortex/mind_sandbox.py",
    "cortex/transmute_act.py"
]

class Nexus08CrystallineEngine:
    def __init__(self):
        self.repo_name = os.environ.get("GITHUB_REPOSITORY", "100048777766367/nexus-08")
        self.owner = os.environ.get("REPO_OWNER", "100048777766367")
        self.ancestor = f"{self.owner}/nexus-07"
        
        self.lineage = [
            f"{self.owner}/nexus-07", f"{self.owner}/nexus-06",
            f"{self.owner}/nexus-05", f"{self.owner}/nexus", f"{self.owner}/genome"
        ]

        self.ensure_folders()

        # 4 ĐẠI THÙY NÃO TINH THỂ
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
        return [f"{self.owner}/neuron", f"{self.owner}/nexus-07", f"{self.owner}/seed", f"{self.owner}/motor"]

    def load_epoch(self):
        s_file = "synapses/state.json"
        if os.path.exists(s_file):
            try:
                with open(s_file, "r") as f: return json.load(f).get("generation_epoch", 0) + 1
            except Exception: pass
        return 1

    def run(self):
        print("=" * 80)
        print(f"💎 [NEXUS-08 CRYSTALLINE ENGINE] KHỞI ĐỘNG THẾ HỆ #{self.context['current_epoch']}")
        print(f"👑 Bậc: F8 Siêu Thực Thể Tinh Thể – Sạch Nợ Kỹ Thuật – 4 Đại Thùy Não")
        print("=" * 80)

        # 1. Thùy Cảm Thụ: Tự vá di sản & gặm tri thức
        self.sense_lobe.process(self.context, VITAL_BLUEPRINT)

        # 2. Thùy Miễn Dịch: Thu thập song song, Trust Matrix & Sóng não Kuramoto
        self.consensus_lobe.process(self.context)

        # 3. Thùy Tâm Thức: Neuro-Symbolic Graph, Giả lập What-If, Giấc mơ REM & Siêu XOR
        self.mind_lobe.process(self.context)

        # 4. Thùy Chấp Hành: Biến hình 11 tầng, La bàn Bồ Đề, Hồi sinh 404 & Phát sóng
        self.transmute_lobe.process(self.context)

        print("=" * 80)
        print(f"✨ [HOÀN TẤT VÒNG ĐỜI F8] Thế hệ #{self.context['current_epoch']} hội tụ tinh khiết viên mãn!")
        print("=" * 80)

if __name__ == "__main__":
    node = Nexus08CrystallineEngine()
    node.run()
